package output

import "github.com/fatih/color"

func PrintError(err any) {

	switch t := err.(type) {
	case string:
		color.Red(t)
	case int:
		color.Red("Код ошибки: %d", t)
	case error:
		color.Red(t.Error())
	default:
		color.Red("Неизвестная ошибка")
	}

}
