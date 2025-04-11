package main

import (
	"fmt"
	"math/rand/v2"
)

// func main() {
// 	a := 5
// 	// pointerA := &a // Это указатель на переменную a. Сама по себе переменная a - int, и поэтому если мы ее используем в функции, и потом, например, перезаписываем в функции значение, то это не мутирует изначальное значение
// 	// С указателем значение будет мутировать, потому что указатель указывает на адрес в памяти
// 	double(&a)
// 	fmt.Println(a)
// 	// fmt.Println(pointerA)  // Здесь выведется адрес переменной в памяти, а не значение
// 	// fmt.Println(*pointerA) // Здесь мы разыменовываем указатель, чтобы получить значение переменной, на которую он указывает
// }

// func double(num *int) {
// 	*num = *num * 2
// } // Если необходимо проводить манипуляции со значением записанным в указатель, то нужно обязательно разыменовать указатель

// Написание функции для вывода реверсного массива
// func main() {
// 	a := [4]int{1, 2, 3, 4}
// 	reverse(&a)
// 	fmt.Println(a)
// }

// func reverse(arr *[4]int) {
// 	for index, value := range *arr {
// 		arr[len(arr)-1-index] = value
// 	}
// }

type account struct {
	login    string
	password string
	url      string
} // Это стракт или структура. Структура это набор полей, которые могут быть разного типа. Структуры это что-то похожее на классы в других языках программирования, но в Go нет наследования и полиморфизма, поэтому структуры это просто набор полей

// Методы страктов
// Методы в основном записываются рядом со страктами
func (acc account) outputData() { // Чтобы объявить метод стракта, нужно указать его имя между объявлением функции и ее именем
	fmt.Println(acc.login, acc.password, acc.url)
}

// Переписываю функцию генерации пароля в метод структуры
func (acc *account) generatePassword(n int) {
	password := make([]rune, n)
	for i := range password {
		password[i] = letterRunes[rand.IntN(len(letterRunes))]
	}
	acc.password = string(password)
}

var letterRunes = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")

func main() {

	// str := []rune("Привет!)") // Это рунный массив. Руна это по alias для int32, который используется для хранения символов в Go. То есть, когда мы хотим пройтись for по строке, то изначально все символы будут переведены в unicode, и если мы хотим получить сами символы, то нужно вызывать функцию string()
	// for _, ch := range string(str) {
	// 	fmt.Println(ch, string(ch))
	// }

	userLogin := promptData("Введите логин: ")
	// userPassword := promptData("Введите пароль: ")
	fmt.Println("Введите сколько символов вы хотите в пароле: ")
	var userPasswordLength int
	fmt.Scan(&userPasswordLength)
	userUrl := promptData("Введите URL: ")

	// account1 := account{
	// 	login,
	// 	password,
	// 	url,
	// } // Можно инстанциировать структуру таким образом, но тогда порядок очень важен. Нужно передавать все в том же порядке, что и в структуре, иначе возникнет путаница
	myAccount := account{
		login: userLogin,
		url:   userUrl,
	} // Если инстранциировать структуру таким образом, то можно записывать в любом порядке
	// При такой записи можно даже пропустить одно значение, и тогда оно будет пустым. Если пропустить какую-либо из переменных в первом случае, то выпадет ошибка

	myAccount.generatePassword(userPasswordLength)
	fmt.Println("Ваш новый пароль: ", myAccount.password)
	myAccount.outputData() // Чтобы вызвать метод структуры, нужно сначала инстанциировать структуру, а потом вызвать метод структуры. Внутри метода можно использовать поля структуры, к которой он относится. То есть, если мы вызываем метод структуры account, то внутри метода мы можем использовать поля этой структуры

	// outputPassword(&myAccount)

}

func promptData(prompt string) string {
	fmt.Print(prompt)
	var res string
	fmt.Scan(&res)
	return res
}

// func outputPassword(acc *account) {
// 	fmt.Println(acc.login, acc.password, acc.url)
// }

// func generatePassword(n int) string {
// 	password := make([]rune, n)
// 	for i := range password {
// 		password[i] = letterRunes[rand.IntN(len(letterRunes))]
// 	}
// 	return string(password)
// }
