package weather

import (
	"Go-learn-part-five/geo"
	"fmt"
	"io"
	"net/http"
	"net/url"
)

// Создаю функцию для получения погоды
func GetWeather(geo geo.GeoData, format int) string {
	baseUrl, err := url.Parse("https://wttr.in/" + geo.City) // Преобразую строку в объект структуры URL. Это нужно, чтобы к URL можно было добавить полученные от пользователя данные
	if err != nil {
		fmt.Println(err.Error())
		return ""
	}
	params := url.Values{}                   // Создаю словарь для параметров URL
	params.Add("format", fmt.Sprint(format)) // Добавляю параметр "format" со значением format, которое получено от пользователя
	baseUrl.RawQuery = params.Encode()       // Преобразую параметры в строку и добавляю к URL
	resp, err := http.Get(baseUrl.String())
	if err != nil {
		fmt.Println(err.Error())
		return ""
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Println(err.Error())
		return ""
	}
	return string(body)
}
