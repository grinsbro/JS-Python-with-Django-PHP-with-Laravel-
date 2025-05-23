package main

import (
	"Go-learn-part-five/geo"
	"Go-learn-part-five/weather"
	"flag"
	"fmt"

	"github.com/fatih/color"
)

func main() {
	color.Green("Сейчас выведем погоду")
	// name := flag.String("name", "Ilia", "Имя пользователя")
	// flag - это встроенный пакет, который позволяет задавать флаги для использования в проекте. Первое значение - название флага, второе - дефолтное значение, а третье - дополнительная информация
	// флаги передаются через двойное тире --

	// age := flag.Int("age", 24, "Возраст пользователя")
	// flag.Parse()
	// Метод Parse() позволяет распарсить значение, которые переданы во флаг, но использовать его нужно только после объявления всех флагов, иначе те, которые были объявлены после парса ббудут иметь только дефолтные значение

	// fmt.Println(*name) // Здесь выводится значение флага name. Обязательно нужно ссылаться на переменную, потому что иначе выведется место в памяти
	// fmt.Println(*age)

	city := flag.String("city", "", "Город пользователя")
	format := flag.Int("format", 2, "Формат вывода погоды")

	flag.Parse()

	// r := strings.NewReader("Привет! Я поток данных") // Создаю reader и записываю его в переменную r
	// block := make([]byte, 4)                         // Создаю буфер - слайс байт длинной в 4 и записываю в переменную block
	// for {
	// 	_, err := r.Read(block)   // Прохожусь по ридеру и записываю данные в буфер. Read возвращает количество обработанных байт и ошибку
	// 	fmt.Printf("%q\n", block) // Вывожу на каждой итерации значение block
	// 	if err == io.EOF {        // Если файл или в данном случае строка закончилась - прерываю цикл
	// 		break
	// 	}
	// }

	geoData, err := geo.GetMyLocation(*city)
	if err != nil {
		fmt.Println(err.Error())
	}
	weatherData := weather.GetWeather(*geoData, *format)

	fmt.Printf("Cейчас: %v", weatherData)
}
