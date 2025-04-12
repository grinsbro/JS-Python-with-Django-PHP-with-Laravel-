package account

import (
	"encoding/json"
	"go-learn-part-four/filemanagement"
	"strings"
	"time"

	"github.com/fatih/color"
)

// Это файл для структуры Vault. Структура Vault это хранилище, где хранятся аккаунты, а также она добавляет возможность работы с данными в файле data.json
// Структура Vault хранит в себе массив аккаунтов, а также дату обновления. Дата обновления нужна для того, чтобы знать, когда последний раз обновлялись данные в файле data.json

type Vault struct {
	Accounts  []Account `json:"accounts"`
	UpdatedAt time.Time `json:"updated_at"`
}

// Здесь я создаю структуру VaultWithDb, которая наследуется от структуры Vault и добавляет поле с названием файла, в котором хранятся данные
// Это нужно, чтобы не передавать имя файла в каждую функцию, а просто использовать его в методах структуры VaultWithDb
type VaultWithDb struct {
	Vault
	db filemanagement.JsonDb
}

// Это конструктор структуры VaultWithDb. Он принимает в значение db имя файла, в котором хранятся данные. Если файл не существует, то он создаст новый файл с пустым массивом аккаунтов и текущей датой обновления
// Если файл существует, то он прочитает данные из файла и запишет их в структуру VaultWithDb. Если не удалось разобрать файл, то он создаст новый файл с пустым массивом аккаунтов и текущей датой обновления
func NewVault(db *filemanagement.JsonDb) *VaultWithDb {

	file, err := db.Read() // Здесь вызывается метод Read из структуры JsonDb
	if err != nil {
		return &VaultWithDb{
			Vault: Vault{
				Accounts:  []Account{},
				UpdatedAt: time.Now(),
			},
			db: *db,
		} // Если не удалось прочитать файл, то создается новый экземпляр структуры VaultWithDb с пустым массивом
	}
	var vault Vault                    // В противном случае создаю переменную экземпляр структуры Vault, в которую будут записаны данные из файла data.json
	err = json.Unmarshal(file, &vault) // Преобразую json файл в структуру Vault. Unmarshal возвращает только ошибку, поэтому записываю данные в одну переменную
	if err != nil {
		color.Red("Не удалось разобрать файл data.json")
		return &VaultWithDb{
			Vault: Vault{
				Accounts:  []Account{},
				UpdatedAt: time.Now(),
			},
			db: *db, // Если не удалось разобрать файл, то создается новый экземпляр структуры VaultWithDb с пустым массивом
		}
	}
	return &VaultWithDb{
		Vault: vault,
		db:    *db,
	} // Если все проверки пройдены, то возвращается экемпляр структуры VaultWithDb с заполненными данными из файла data.json
}

func (vault *VaultWithDb) AddAccount(acc Account) {
	vault.Accounts = append(vault.Accounts, acc)
	vault.save()
}

func (vault *VaultWithDb) FindAccountsByUrl(url string) []Account {
	var accounts []Account
	for _, data := range vault.Accounts {
		isMatched := strings.Contains(data.Url, url)
		if isMatched {
			accounts = append(accounts, data)
		}
	}
	return accounts
}

func (vault *VaultWithDb) DeleteAccountByUrl(url string) bool {

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

func (vault *Vault) ToBytes() ([]byte, error) { // Это метод структуры Vault, потому что нужно преобразовать только данные из структуры Vault в json формат
	// Здесь не нужно использовать VaultWithDb, потому что в db хранится название файла, а эти данные не нужны для преобразования в json формат
	file, err := json.Marshal(vault)
	if err != nil {
		return nil, err
	}
	return file, nil
}

func (vault *VaultWithDb) save() {
	vault.UpdatedAt = time.Now()
	data, err := vault.Vault.ToBytes() // Здесь используется вызов vault.Vault, потому что это метод структуры Vault, а не VaultWithDb
	if err != nil {
		color.Red("Не удалось преобразовать")
	}
	vault.db.Write(data)
}
