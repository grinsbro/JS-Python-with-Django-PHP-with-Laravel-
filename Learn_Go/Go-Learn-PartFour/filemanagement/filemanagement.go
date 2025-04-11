package filemanagement

import (
	"fmt"
	"os"

	"github.com/fatih/color"
)

func ReadFile(name string) ([]byte, error) {
	color.Green("Reading file")
	// file err := os.Open("test.txt") // Таким образом открывается файл, но таким образом файл читается по байтам
	data, err := os.ReadFile(name) // Таким образом файл читается целиком. Это можно использовать, когда файл небольших размеров
	if err != nil {
		fmt.Println(err)
		return nil, err
	}
	// fmt.Println(data) // Это байтовый массив, который нужно преобразовать в строку
	// fmt.Println(string(data))
	return data, nil
}

func WriteFile(content []byte, name string) {
	color.Blue("Writing file")
	file, err := os.Create(name) // Таким образом создается файл. Используется встроенный пакет os для работы с файловой системой компьютера, а затем вызывается метод Create, который создает файл с указанным именем
	if err != nil {
		fmt.Println(err)
	}
	// _, err = file.WriteString(content) // Таким образом в файл записываются данные. В данном случае записывается строка, но также есть метод Writebyte, который записывает байты
	_, err = file.Write(content)
	defer file.Close() // Ключевое слово defer откладывает выполнение кода на конец стек фрейма. То есть то, что написано в defer, то выполнится самым последним
	// Также если использовать несколько defer, то последним выполнится самый первый defer
	if err != nil {
		fmt.Println(err)
		return
	}
	color.Green("Запись успешна")
}
