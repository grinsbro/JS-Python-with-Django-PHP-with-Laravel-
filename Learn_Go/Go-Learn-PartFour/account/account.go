package account

// Если необходимо вынести какой-то функционал в отдельный пакет, то необходимо в корне проекта создать папку, которая будет называться также как и пакет, и в ней создать файл

import (
	"errors"
	// "fmt"
	"math/rand/v2"
	"net/url"
	"time"

	"github.com/fatih/color"
)

var letterRunes = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*")

type Account struct {
	login    string
	password string
	url      string
}

type accountWithTimeStamp struct {
	createdAt time.Time
	updatedAt time.Time
	Account   // Это встраивание структуры. То есть при инстанциировании структуры accountWithTimeStamp, в ней будет доступна структура account
}

func (acc *Account) OutputData() { // Чтобы объявить метод стракта, нужно указать его имя между объявлением функции и ее именем
	color.Cyan(acc.login)
	// fmt.Println(acc.login, acc.password, acc.url)
}

func (acc *Account) generatePassword(n int) {
	password := make([]rune, n)
	for i := range password {
		password[i] = letterRunes[rand.IntN(len(letterRunes))]
	}
	acc.password = string(password)
}

func newAccount(login, password, urlString string) (*Account, error) { // Общепринято называть конструкторы по имени структуры добавляя new в начале
	if login == "" {
		return nil, errors.New("login cannot be empty")
	}
	_, err := url.ParseRequestURI(urlString)
	if err != nil {
		return nil, errors.New("invalid URL")
	}
	newAcc := &Account{
		login:    login,
		password: password,
		url:      urlString,
	}
	if password == "" {
		newAcc.generatePassword(8)
	}
	return newAcc, nil
}

// Чтобы экспортировать функцию, ее название должно быть с большой буквы
func NewAccountWithTimeStamp(login, password, urlString string) (*accountWithTimeStamp, error) { // Общепринято называть конструкторы по имени структуры добавляя new в начале
	if login == "" {
		return nil, errors.New("login cannot be empty")
	}
	_, err := url.ParseRequestURI(urlString)
	if err != nil {
		return nil, errors.New("invalid URL")
	}
	newAcc := &accountWithTimeStamp{
		createdAt: time.Now(),
		updatedAt: time.Now(),
		Account: Account{
			login:    login,
			password: password,
			url:      urlString,
		}, // Так зыписывается логика создания инстанции структуры, которая наследует другую структуру
	}
	if password == "" {
		newAcc.generatePassword(8) // Такая запись все равно валидна, потому что мы инстанциировали структуру account внутри структуры accountWithTimeStamp, и поэтому у нас есть доступ к методу generatePassword
	}
	return newAcc, nil
}
