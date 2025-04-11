package filemanagement

import (
	"fmt"
	"os"

	"github.com/fatih/color"
)

func ReadFile() {
	color.Green("Reading file")
	// file err := os.Open("test.txt") // Таким образом открывается файл, но таким образом файл читается по байтам
	data, err := os.ReadFile("test.txt") // Таким образом файл читается целиком. Это можно использовать, когда файл небольших размеров
	if err != nil {
		fmt.Println(err)
		return
	}
	// fmt.Println(data) // Это байтовый массив, который нужно преобразовать в строку
	fmt.Println(string(data))
}

func WriteFile(content string, name string) {
	color.Blue("Writing file")
	file, err := os.Create(name) // Таким образом создается файл. Используется встроенный пакет os для работы с файловой системой компьютера, а затем вызывается метод Create, который создает файл с указанным именем
	if err != nil {
		fmt.Println(err)
	}
	_, err = file.WriteString(content) // Таким образом в файл записываются данные. В данном случае записывается строка, но также есть метод Writebyte, который записывает байты
	defer file.Close()                 // Ключевое слово defer откладывает выполнение кода на конец стек фрейма. То есть то, что написано в defer, то выполнится самым последним
	// Также если использовать несколько defer, то последним выполнится самый первый defer
	if err != nil {
		fmt.Println(err)
		return
	}
	color.Green("Запись успешна")
}
