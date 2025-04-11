package account

import (
	"encoding/json"
	"go-learn-part-four/filemanagement"
	"strings"
	"time"

	"github.com/fatih/color"
)

type Vault struct {
	Accounts  []Account `json:"accounts"`
	UpdatedAt time.Time `json:"updated_at"`
}

func NewVault() *Vault {

	file, err := filemanagement.ReadFile("data.json")
	if err != nil {
		return &Vault{
			Accounts:  []Account{},
			UpdatedAt: time.Now(),
		}
	}
	var vault Vault
	err = json.Unmarshal(file, &vault)
	if err != nil {
		color.Red("Не удалось разобрать файл data.json")
		return &Vault{
			Accounts:  []Account{},
			UpdatedAt: time.Now(),
		}
	}
	return &vault
}

func (vault *Vault) AddAccount(acc Account) {
	vault.Accounts = append(vault.Accounts, acc)
	vault.save()
}

func (vault *Vault) FindAccountsByUrl(url string) []Account {
	var accounts []Account
	for _, data := range vault.Accounts {
		isMatched := strings.Contains(data.Url, url)
		if isMatched {
			accounts = append(accounts, data)
		}
	}
	return accounts
}

func (vault *Vault) DeleteAccountByUrl(url string) bool {

	var accounts []Account
	isDeleted := false

	for _, data := range vault.Accounts {
		isMatched := strings.Contains(data.Url, url)
		if !isMatched {
			accounts = append(accounts, data)
			continue
		}
		isDeleted = true
	}
	vault.Accounts = accounts
	vault.save()
	return isDeleted
}

func (vault *Vault) ToBytes() ([]byte, error) {
	file, err := json.Marshal(vault)
	if err != nil {
		return nil, err
	}
	return file, nil
}

func (vault *Vault) save() {
	vault.UpdatedAt = time.Now()
	data, err := vault.ToBytes()
	if err != nil {
		color.Red("Не удалось преобразовать")
	}
	filemanagement.WriteFile(data, "data.json")
}
