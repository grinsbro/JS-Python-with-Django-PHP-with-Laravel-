// const obj1 = {
//     name: 'Ilich',
//     age: 24,
// }
// const obj2 = {
//     name: 'Ilich',
//     age: 24,
// }

// const areObjectsEqual = (object1, object2) => {
//     const keys1 = Object.keys(object1)
//     const keys2 = Object.keys(object2)

   
//     if (keys1.length !== keys2.length) {
//         return false
//     }
    
    
//     for (const key in object1) {
//        const value1 = object1[key]
//        const value2 = object2[key]
//        const areValuesObjects = 
//        typeof value1 === 'object' && typeof value2 === 'object'
       
//        if (areValuesObjects) {
//         return areObjectsEqual(value1,value2)
//        }

//        if (value1 !== value2) {
//         return false
//        }
//     }
//     return true
// }

// console.log (
//     "Are objects obj1 & obj2 equal?",
//     areObjectsEqual(obj1,obj2)
// )


// const obj1 = {name: 'Ilich'}
// const obj2 = Object.assign({}, obj1)

// console.log(obj1)
// console.log(obj2)

// const obj1 = {name: 'Ilich'}
// const obj2 = {age: 24}

// const user = Object.assign({}, obj1, obj2)

// console.log("User:", user)


// const userAddress = ({city, street, houseNumber, apartmentNumber}) => {
//     console.log(`
//         Адрес:
//         г. ${city}, ул. ${street},
//         д. ${houseNumber}, кв. ${apartmentNumber}`)

// }

// userAddress ({
//     city: "Mосква",
//     street: "Профсоюзная",
//     houseNumber: "28",
//     apartmentNumber: "57"
// })

// console.log ('this global:', this)

// function fn() {
//     console.log('this in function:', this)
// }

// fn()

// const user = {
//     name: 'Ilich',
//     age: 24,
//     logThis: function () {
//         console.log ('This in method object user:', this)

//     },
// }

// user.logThis()

// const calculator = {
//    read() {
//     this.a = Number(prompt('Введите первое число:', 0))
//     this.b = Number(prompt('Введите второе число:', 0))
  
//    },
//    sum() {
//     return this.a + this.b
//    },
//    mul() {
//     return this.a * this.b
//    }, 
// }

// calculator.read()
// console.log("calculator", calculator)
// console.log('Сумма: ', calculator.sum())
// console.log("Произведение: ", calculator.mul())


// const userAdress = ({city, zip, address, houseNumber}) => {
//     console.log( 
//         `Адрес пользователя:
//         Город: ${city};
//         Индекс: ${zip};
//         Улица: ${address};
//         Номер дома: ${houseNumber}` 
//     )
// }

// userAdress ({
//     city: "Москва",
//     zip: 117209,
//     address: "Севастопольский проспект",
//     houseNumber: '28к7'
// })


//Метод toFixed
/* 
const price = 45.9102

console.log(price.toFixed(2))

console.log((5.92204521).toFixed(2))

console.log(100..toFixed(2))
*/
// метод toPrecision
/*
const number = 190.23211

console.log(`toprecision: `, number.toPrecision(4))
console.log(`toFixed: `, number.toFixed(4))
*/
// toString
/*
const num = 100
const numAsString = num.toString()
console.log(`Num as number: `, num)
console.log(`Num as string: `, numAsString)

console.log(typeof num)
console.log(typeof numAsString)
*/
// Math functions
/*
console.log(`Random number: `, Math.random()) // Рандомное число от 0 до 1

console.log(Math.abs(-29)) //Это отбрасывает минус у числа

console.log(Math.pow(2,10)) //Возведение в степень. Первое это число, а второе степень

console.log(Math.sqrt(25)) // Квадратный корень из числа

console.log(Math.cbrt(127)) //кубический корень

console.log(Math.min(1,2,5,-200,-1000,0,2000)) //минимальное число из рядка

console.log(Math.max(1,0,2,5,-11000,210232134,4,5)) //максимальное число из ряда

console.log(Math.round(3.49)) //округление до ближайшего по правилам

console.log(Math.floor(3.85)) // округление вниз

console.log(Math.ceil(3.10)) // округление вверх

console.log(Math.trunc(-3.49)) // округление вниз без учета минуса
*/

// Парсинг
/*
const numberAsString = `100.5px`

console.log(parseInt(numberAsString)) // Парсинг целых чисел записанных как строка

console.log(parseFloat(numberAsString)) // Парсинг дробных чисел записанных как строка
*/

//МЕТОДЫ СТРОК
/*
const name = 'Ilich'

console.log(name[4]) // Получить символ из строки

console.log(name.at(-2)) // чтобы работать с последними символами строк удобнее

const text = 'TeXt To cHaNgE rEgIsTeR'

console.log(text.toLowerCase()) // Перевести в нижний регистр

console.log(text.toUpperCase()) // Перевести в верхний регистр

const message = '    Hello      '

console.log(message.trim()) // убрать пробелы в начале и в конце

console.log(message.trimEnd()) // убрать пробелы в конце

console.log(message.trimStart()) // убрать пробелы в начале

const longMessage = 'Пробую найти ~это выражение~ в этом предложении'

console.log(
    longMessage.indexOf(`~это выражение~`) // Чтобы найти индекс первого символа в искомом тексте
)

console.log(
    longMessage.includes(`~это выражение~`) // Чтобы просто проверить есть ли такой текст в строке
)

// Также есть методы .startsWith и endsWith. Они нужны, чтобы проверить начинается или заканчивается с предполагаемых символов строка

const str = 'JavaScript'

console.log(str.substring(0,4)) // Чтобы вырезать определенный текст из строки

console.log(str.slice(0,4)) // Чтобы вырезать определенный текст из строки

console.log(str.repeat(5)) // повторяет строку сколько надо

const messageToReplace = `Я изучаю бэкенд, но я еще ничего не знаю про бэкенд`

console.log(
    messageToReplace.replace(`бэкенд`, `фронтенд`) // меняет опредленный текст на тот, который нужно, но только в первый раз где встречается
)

console.log(
    messageToReplace.replaceAll(`бэкенд`, `фронтенд`) // меняет определенный текст на тот, который нужно везде
)
console.log(
    messageToReplace.replace(/бэкенд/gi, `фронтенд`) // меняет опредленный текст на тот, который нужно везде с replace. i добавляется, чтобы искать и по регистру
)

const number = `+7 (999) 829 20 42`
console.log(
    number.replace(/\d/g, `#`) // Чтобы поменять вссе цифры на нужный текст
)

const splituy = `Привет, мир!`

console.log(
    splituy.split(`, `) // делит строку на массив по заданному разделителю
)

// все эти методы не изменяют строку навсегда. Они работают только когда их вызывают

// Как применять на примере алерт и промпт

const value = prompt(`Введите ваше имя:`)

const clearValue = value.trim().toLowerCase()

if (clearValue.length === 0) {
    alert(`Ошибка! Имя не может быть пустым.`)
}

if (clearValue.includes(`админ`)) {
    alert("Ошибка! Вы не можете занять это имя.")
}
*/
// МАССИВЫ [Основы]
/*
const arr = ['Hello',
    100,
    true,
] // В массиве могут быть любые типы данных, даже массив

console.log('arr:', arr)

console.log(arr[0]) // чтобы вывести объект под определенным индексом из массива

// console.log(arr[3].name) или ['name'] // Чтобы вывести значение объекта из массива

 // arr[4]() // чтобы вызвать функцию из массива

 // console.log(arr[5][0]) // чтобы обратиться к первому объекту из массива в массиве

 const matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ]
console.log(matrix[1][0])

arr[0] = 'Bye-bye' //переприсваивает значение переменным в массиве
console.log(arr[0])

console.log(arr[arr.length-1]) // Чтобы получить последний элемент массива

console.log(arr.at(-1)) // также чтобы вывести последний элемент массива

const letters = ['A', 'B', 'C']

console.log('Letters before:', letters)

letters.push('D') // Вставляет элемент в конец массива

console.log('Letters after adding element in the end: ', letters)

letters.unshift('Z','Y') // добавляет элементы в начало массива

console.log('Letter after adding element in the beginning: ', letters)

letters.pop() // удаляет последний элемент в массиве

console.log('Letters after deleting last element: ', letters) 

letters.shift() // Удаляет первый элемент в массиве

console.log('Letters after deleting initial element: ', letters)

console.log(arr.toString()) // Чтобы преобразовать массив в строку

console.log(arr.join(', ')) // Также можно использовать для преобразования в строку

const message = 'One, Two, Three, Four, Five'

console.log(
    message.split(', ').join(', ')
)

const arr1 = ['A','B','C', []]
const arr2 = ['A','B','C', []]
// const arr2 = [...arr1] // или arr1.slice(в скобках пишу элементы с какого по какой скопировать значения) // Копирует массив, чтобы можно было изменять только копию, но не оригинал
// console.log('arr1: ', arr1)

// console.log('arr2: ', arr2)

const arr3 = ['D','E','F']
const arr4 = ['G','H','I']

const arr3n4 = [...arr3, ...arr4] // или можно указать arr3.concat(arr4) Это тоже объединяет массивы // Чтобы объединить два массива

console.log(arr3n4)

console.log(arr1 == arr2)

const areArraysEqual = (array1, array2) => {
    if (array1.length !== array2.length) {
        return false
    }

    for (let i = 0; i < array1.length; i++) {
        const value1 = array1[i]
        const value2 = array2[i]


        const areValuesArrays = 
            Array.isArray(value1) && Array.isArray(value2)

            if (areValuesArrays) {
               if (!areArraysEqual(value1,value2)) {
                return false
               } else {
                continue
               }
            } // Вот это добавялется, если в массиве есть еще массивы, но пустые

        if (value1 !== value2) {
            return false
        }
    }

    return true
}

console.log(areArraysEqual(arr1,arr2)) // Функция сравнивает два массива, но только когда там примитивные элементы
*/

// Методы Массивов
/*
const Data = ["Ilich", 24]

const [name, age] = Data // Деструктуризация массива (ПОРЯДОК ПЕРЕМЕННЫХ ВАЖЕН!!!!!)

console.log('Name: ', name)
console.log('Age: ', age) 

const letters = ['A', 'B', 'C', 'D', 'E', 'F']

letters.forEach((letter, i, array) => {
    console.log(`По индексу [${i}] находится элемент "${letter}`)
}) // используется, чтобы перебрать массив

const prices = [100, 200, 400, 50000, 20000, 400]

console.log(prices.indexOf(400)) //ищет индекс определенного элемента массива

console.log(prices.indexOf(400,3)) // после запятой пишем с какого индекса начинаем поиск

console.log(prices.lastIndexOf(400)) // ищет с конца

const users = [
    {
        name: 'Ilich',
        age: 24,
        city: 'Paphos' 
    },
    {
        name: 'Sam',
        age: 24,
        city: 'Moscow'
    },
    {
        name: 'Sam',
        age: 30,
        city: 'Baku'
    },
    {
        name: 'Maga',
        age: 25,
        city: 'Moscow'
    },
]

console.log(
    users.findIndex((user) => {
        if (user.name === 'Maga') {
            return true
        }
    })
) // чтобы перебрать массив, когда там есть непримитивные элементы и получить индекс этого элемента

console.log(
    users.findIndex((user) => user.name === 'Maga')
) // упрощенный вариант предыдущего

console.log(prices.includes(100)) // Чтобы узнать есть ли элемент в массиве

console.log(
    users.some((user) => user.name === 'Maga')
) // Чтобы узнать есть ли элемент в массиве, когда там непримитивные элементы

console.log(
    users.every((user) => user.age >= 18 )
) // Чтобы проверить все элементы на соответствие определенному условию

console.log(
    users.find((user) => user.name === 'Sam')
) // ищет элемент по соответствию определенному условию, но только первый

console.log(
    users.filter((user) => user.name === 'Sam')
) // ищет все элементы по соответствию определенному условию и возвращает массив

console.log(
    users.filter((user) => user.city === 'Moscow')
)
//ИЛИ

const filterUsers = users.filter((city, age) => {
    return city === 'Moscow' || age < 29
})

const usersFormatted = users.map((user) => {
    return `${user.name} is ${user.age} years old and lives in ${user.city}`
}) // переформатирует данные из массива в то, что нужно сделать, но не изменяет его! Он только возвращает значение

console.log(usersFormatted)

const ageSum = users.reduce((sum, user, indexedDB, array) => {
    return sum + user.age
}, 0) // перебирает и аккумулирует элементы из массива (Если надо перебрать элементы справа налево, то пишем .reduceRight)

console.log(
    'Средний возраст пользователей: ',
    ageSum / users.length
)

console.log(
    'Массив в нормальном порядке: ',
    users
)

const reversedUsers = users.reverse() // Этот метод переворачивает массив с конца на начало и МУТИРУЕТ оригинальный массив. Чтобы не мутировать оригинальный массив, то надо написать [...users].reverse()
console.log(
    'Массив в обратном порядке: ',
    reversedUsers
)

const names = ['Ilich', 'Sam', 'Maga', 'Anton', 'Barn']

const sortedNames = names.sort() // сортирует исходный массив и МУТИРУЕТ его, если не нужно, то работаем с копией 
console.log(
    'Sorted names: ',
    sortedNames
)

const numbers = [500, 1, 4]

const sortedNumbers = numbers.sort() // если надо сортировать по убыванию числа, то пишем .sort((a,b) => b - a)

console.log(
    'Sorted numbers: ',
    sortedNumbers
)
*/

// Перебор объекта в JavaScript. Коллекции Map и Set
/*
const user = {
    name: 'Ilich',
    age: 24,
    City: 'Paphos'
}
const userKeys = Object.keys(user) // Перебирает объект в массив и содержит ключи, а не значения

console.log('userkeys: ', userKeys)

const userValues = Object.values(user) // Перебирает объект в массив и содержит значения

console.log('uservalues: ', userValues)

const userEntries = Object.entries(user) // Перебирает объект в массивы, которые содержат и ключи, и значения

console.log('userentries: ', userEntries) 

const userEntries2 = Object.entries(user)

const userFormatted = userEntries2.map(([key, value]) => {
    return [key.toUpperCase(), `~~${value}~~`]

})

console.log(userFormatted)

const arrToObj = Object.fromEntries(userFormatted) // возвращает из массива объект

console.log(arrToObj)

const data = new Map([
    [1, 'One as a number'],
    ['1', 'One as a string']
]) // Используется, чтобы записать в ключи объекта два вида данных строчные и числовые

const data2 = new Map()

data2.set(1, 'One as a number') // Чтобы динамически добавить в коллекцию map значения
data2.set('1', 'One as a string')

console.log(data2.get(1))
console.log(data2.get('1')) // чтобы обратиться к коллекции map по ключу

data2.set('name', 'Ilich')

console.log(data2.has('name')) // чтобы проверить есть ли в коллекции данные с таким ключом (возвращает только true или false, а не само значение ключа)

data2.delete('name')

console.log(data2.has('name'))

data2.clear // очищает всю коллекцию map

console.log(data2.size) // возвращает количество пар ключ/значение

const set = new Set([1,2,2,2,3]) // Коллекция, которая содержит только значения, НО в единственном виде. В консоли ниже видно, что выводит только одну 2, хотя их 3 в массиве

console.log(set)

set.add('Ilich') // добавляет значение в коллекцию

console.log(set)

// set.delete('Ilich') // удаляет значение

// set.has(1) // проверяет наличие в колллекции значения

// set.size // возвращает длину коллекции

// set.clear // очищает коллекцию

set.add('Sam')
set.add('Maga')

for (const key of set.keys()) {
    console.log('key: ', key)
}
for (const value of set.values()) {
    console.log('key: ', value)
}
for (const entry of set.entries()) {
    console.log('key: ', entry)
}

console.log('set values: ')
set.forEach((value) => {
    console.log(value)
})
*/

// JavaScript и JSON формат — парсинг и преобразование данных
/*
const user = {
    name: 'Ilich',
    age: 24,
    city: 'Paphos',
    adress: {
        street: 'Agiou Markou 4',
        zipcode: 8201
    },
    todo: ['sleep','eat', 'work', 'learn'],
    hasdog: false,
    yacht: null
}
const userDataAsString = JSON.stringify(user) // Преобразует объекст в строку правильно, чтобы отправить на сервер

console.log(userDataAsString)

const parseUserData = JSON.parse(userDataAsString) // наоборот переделывает из строки в объект

console.log(parseUserData)

// Если в объекте есть значения undefined или методы, то stringify их проигнорирует
*/

// Классы в JavaScript — объявление, конструктор, наследование, экземпляр, геттеры и сеттеры
/*
class Student {
    planet = 'Earth'
    country = 'Russia'
    region // это свойства, которые добавляеются по умолчанию всем элементам класса
    constructor(name, age) {
        this.name = name
        this.age = age 
    } // Так добавляются динамическе свойства, которые задаются в момент создания элемента

    logAge(){
        console.log(this.age)
    }

    set city(value) {
        const firstLetter = value[0].toUpperCase()
        const fromSecondLetter = value.slice(1).toLowerCase()

        this._city = `${firstLetter}${fromSecondLetter}`
    } // Это называется сеттер. Он создает свойство. То, что там написано это переделка, чтобы город, например, всегда писался с большой буквы, даже если ее написали с маленькой  
    // нижнее подчеркивание означает, что свойство имеет отношение к только данному классу (или объекту, если бы он был), то есть извне к нему не стоит обращаться
    get city() {
        return `city: ${this._city}`
    } // Это геттер, он вытягивает значение из уже созданного свойства



} // Так создается класс (всегда с большой буквы)

const firstStudent = new Student('Ilich', 24)
const secondStudent = new Student('Sam', 24)

console.log('First student: ', firstStudent)
console.log('Second student: ', secondStudent)

console.log('Name of the first student: ', firstStudent.name)
console.log('Name of the second student: ', secondStudent.name)

firstStudent.logAge()
secondStudent.logAge()

firstStudent.city = 'moscow'

console.log(firstStudent.city)

class Person {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    eat() {console.log('Ем....')}
    sleep() {console.log('Сплю....')}
}

const examplePerson = new Person('Ильич', 24)

class Developer extends Person {

    constructor(name,age,experience) {
        super(name,age)
        this.experience = experience
    }

    writeCode() {console.log('Пишу код....')}
    
    sleep() {
        console.log('Не хочу спать, пойду писать код....')
        this.writeCode()
    }
} // таким образом наследуются классы extends означает, что новый класс будет иметь все то же, что и предыдущий, но еще и выполнять свои методы или иметь свойства

class JavaScriptDeveloper extends Developer {
    makeFrontend() {'Пишу фронтенд....'}

    eat() {
        super.eat() // super используется, когда нужно написать код, который уже есть в наследуемом классе. Нужно, чтобы оптимизировать код
        console.log('Смотрю ютуб...')
    }
}

const jsDeveloperExample = new JavaScriptDeveloper ('Ильич', 24)

jsDeveloperExample.eat()
*/

// JavaScript Отложенное и регулярное выполнение кода — setTimeout и setInterval, clearTimeout и др.
/*
setTimeout(() => {
    alert('Это уведомление отобразится спустя 2 секунды после загрузки страницы')
}, 2000) // Таким образом устанавливается таймер на выполнение какой-то функции. Можно использовать стрелочную запись, писать функцию полностью или вызывать по имени переменной. Второе значение это время в милисекундах. Последующие параметры это то, что функция ожидает, чтобы в нее передали


const logMessage = () => {
    alert('Message')
}

const timerId = setTimeout(logMessage, 3000) // чтобы потом можно было отменить таймер, нужно записать его в переменную

clearTimeout(timerId) // Так таймер отменяется


const intervalID = setInterval(() => {
    console.log('Hi')
}, 1000) // Так устанавливается интервал, через который функция выполняется

// clearInterval(intervalID) // отменяет выполнение интервала

setTimeout(() => {
    clearInterval(intervalID)
}, 5000) // таким образом можно установить таймер, когда заканчивать интервал


setTimeout(function logmessage() {
    alert('Message once in a second')
    
    setTimeout(logmessage, 1000)
}, 1000) // Это более чистый вид интервала, который учитывает, что предыдущее окно вызванное функцией закрыто, а не отправляет бесконечно раз в секунду
*/

// Обработка ошибок в JavaScript — try catch finally, throw, класс Error
/*
console.log('Начало кода')

try {
    const names = ['Ильич', 'Сэм', 'Мага']
    names.forEach((name) => {
        console.log('Имя: ', name)
    }) // с помощью try изолируется код, который надо проверить на ошибки. То есть если есть ошибка весь последующий код все равно выполнится
} catch (error) {
    console.log('Ошибка: ', error)
} // С помощью catch выводится ошибка, если она есть в try, но последующий код все равно выполняется

console.log('Конец кода')


console.log('Начало кода')

setTimeout(() => {
    try {
        const names = undefined

        names.forEach ((name) => {
            console.log('Имя: ', name)
        })
    } catch (error) {
        console.log('Ошибка: ', error)
    }
    
    console.log('Конец кода')
}, 3000) // Таким образом можно улавливать ошибки в асинхронном коде, то есть том, который выполняется не сразу


try {
    const names = undefined

    names.forEach((name) => {
        console.log('Имя: ', name)
    })

    console.log('Код в блоке try отработал успешно!')
} catch (error) {
    console.log('Ошибка:', error)
} finally {
    console.log('Выполнить в любом случае ') // в finally записывается код, который выполняется в любом случае. Если есть ошибка или ее нет
}
*/

// JavaScript событийный цикл Event Loop, асинхронный код, промисы (Promise), async / await

/**
 * Promise - специальный объект надстройка
 * для работы с асинхронным кодом
 */

/**
 * Promise имеет 3 состояния:
 * pending - исходное состояние
 * fulfilled - выполнено успешно, получен результат
 * rejected - выполнение с ошибкой
 */

/**
 * Основные методы Promise:
 * then() - обрабатывает fulfilled состояние
 * catch() - обрабатывает rejected состояние
 */
/*
const promise = new Promise((fulfill, reject) => {
    console.log('Начало, состояние pending...')
    
    setTimeout(() => {
        if (Math.random() > 0.5) {
            fulfill('Ура, состояние fulfilled')
        } else {
            reject('Увы, состояние rejected')
        }
    }, 3000);
})

promise
    .then((successData) => {
        console.log('Успех! Получены данные: ', successData)
    })
    .catch((errorData) => {
        console.log('Ошибка. Получены данные: ', errorData)
    })
    .finally(() => {
        console.log('Код, который выполняется в любом случае')
    })

async function getSomething() {
    return new Promise((fulfill) => {
        setTimeout(() => {
            fulfill('Hello')
        }, 3000);
    })
}
console.log('Начало')

const something = await getSomething()

console.log(something)

console.log('Конец')
*/

// Модули в JavaScript, import и export, декомпозиция кода
/*
import { initTabs } from "./tabs.js";
import { initModals } from "./modals.js";
import { initSliders } from "./sliders.js";

initTabs()
initModals()
initSliders()

// import * as constants from "./constants.js"; // Так можно импортировать все переменные из файла, чтобы не перечислять их все

// console.log(constants.a) // Так они будут вызываться
// console.log(constants.b)
// console.log(constants.c)
// constants.default() // Так вызывается переменная экспортируемая по умолчанию
*/

// JavaScript в браузере — DOM (Document Object Model) и BOM (Browser Object Model)
// DOM в JavaScript — Навигация по элементам дерева, атрибуты async и defer
// JavaScript DOM. Поиск элементов: getElement и querySelector
/*
const buttonElement = document.getElementById('myButton') // этот метод используется для того, чтобы не перебирать DOM дерево по большому количеству уровней, а сразу обратиться к нудному элементу

console.log('buttonElement', buttonElement)

const buttonElement = document.querySelector('button') // Также можно обратиться таким образом, если у элемента нет id
// или
const buttonElement1 = document.querySelector('.mybutton')

console.log('Button', buttonElement1)

const listItemElements = document.querySelectorAll('.list .item') //Так можно обратиться к множеству вложенных элементов

console.log('Elements of the list:', listItemElements)

listItemElements.forEach((element) => {
    console.log('Element ofthe list:', element)
})

const thirdBoxElement = document.querySelector('.box-3')

const firstBoxElement = thirdBoxElement.closest('.box-1') // Так можно обратиться изнутри иерархии вверх

console.log('FirstBoxElement:', firstBoxElement)
*/

//JavaScript DOM-элементы: свойства и атрибуты, поведение value, data-* атрибуты
/*
getAttribute // Позволяет получить значение атрибута присвоенного элементу из DOM дерева
setAttribute // Позволяет установить значение атрибута для элемента DOM дерева (qwerty, "1")
*/
// DOM JavaScript: стили и CSS-классы. Свойства style и classList. Управление CSS-переменными в JS.
/*
const boxElement = document.querySelector('.box')

console.log(
    boxElement.style //Таким образом можно обратиться к свойству style элемента, но только если он указан в разметке html
)

boxElement.style.position = 'absolute' // Таким образом можно изменять параметры
boxElement.style.top = '40px'
boxElement.style.left = '80px'

boxElement.style.width = '200px'
boxElement.style.borderWidth = '5px'

boxElement.style.cssText += `
    position: absolute;
    top: 40px;
    left: 90px;
    width: 80px;
    border-width: 10px;
`
// Также можно записывать и таким образом, чтобы не писать много раз одно и то же


console.dir(boxElement)

console.log(boxElement.style)

console.log('Значение параметра width у boxElement', boxElement.style.width)

console.log('Вычисление значения стилей boxElement:', getComputedStyle(boxElement).width) //Если стиль записан в css файле, то получить его атрибуты можно через эту команду

console.log('Вычисление значения text-decoration у псевдоэлемента after:', getComputedStyle(boxElement, '::after').textDecoration) //Таким образом уже можно получить атрибут стиля у псевдоэлемента

console.dir(boxElement)

boxElement.classList.add('red', 'big') //Таким образом добавляются классы элементам

boxElement.classList.remove('red') //Таким образом классы удаляются

boxElement.classList.toggle('red') //Таким образом можно управлять классами. Он добавляет указанный класс, если его нет и удаляет его, если он уже есть

const hasError = true

boxElement.classList.toggle('big', false) // Вторым значением можно записать булевое значение при выполнении какого-то процесса

boxElement.style.setProperty('--border-color', 'blue') // таким образом можно управлять css переменными
*/

// Браузерный JavaScript: размеры и координаты DOM-элементов
/*
const boxElement = document.querySelector('.box')

console.log('Полная ширина', boxElement.offsetWidth)
console.log('Полная высота', boxElement.offsetHeight) // Эти параметры выводят полные значение ширины или высоты, учитывая padding border и тд

console.log('Ширина левой рамки', boxElement.clientLeft)
console.log('Ширина верхней рамки', boxElement.clientTop) // Показывает размеры border

console.log('Ширина без учета рамки и скроллбара', boxElement.clientWidth)
console.log('Высота без учета рамки и скроллбара', boxElement.clientHeight) // Показывает ширину или высоту элемента без учета рамки и скроллбара

console.log(
    'Ширина без учета рамки включая прокручиваемую область',
    boxElement.scrollWidth
)

console.log(
    'Высота без учета рамки включая прокручиваемую область',
    boxElement.scrollHeight
) // Показывает высоту или ширину элемента без рамки, но с учетом области, которую можно пролистать (если такая есть)

boxElement.scroll(0, 20) // Позволяет прокрутить любой DOM-элемент по вертикали и горизонтали (x,y)

console.log(
    'Ширина невидимой уже прокрученной по вертикали области',
    boxElement.scrollTop
)
console.log(
    'Высота невидимой уже прокрученной по вертикали области',
    boxElement.scrollLeft
) // Показывает высоту или ширину уже прокрученной области

const boxElementRectParam = boxElement.getBoundingClientRect() // Позволяет получать данные о расположении объекта относительно окна браузера

console.log(boxElementRectParam)

console.log('Координаты левого верхнего угла относительно окна:',
    boxElementRectParam.x,
    boxElementRectParam.y
)
console.log('Координаты правого верхнего угла относительно окна:',
    boxElementRectParam.right,
    boxElementRectParam.top
)
console.log('Координаты левого нижнего угла относительно окна:',
    boxElementRectParam.left,
    boxElementRectParam.bottom
)
console.log('Координаты правого нижнего угла относительно окна:',
    boxElementRectParam.right,
    boxElementRectParam.bottom
) // все эти команды позволяют узнать позиционирование элемента относительно окна браузера

console.log('Координаты позиции скрола страницы:',
    window.scrollX,
    window.scrollY
)

console.log('Координаты левого верхнего угла относительно страницы:',
    boxElementRectParam.x + window.scrollX,
    boxElementRectParam.y + window.scrollY
) //Таким образом можно узнать позиционирование объекта относительно страницы, а не окна
*/

// JS в браузере: размеры окна и страницы, скролл scrollIntoView, scrollTo, scroll, scrollBy
/*
const htmlElement = document.documentElement

console.log(
    'Ширина окна:', htmlElement.clientWidth
)// Так можно посмотреть ширину окна

console.log(
    "Высота окна", htmlElement.clientHeight
)// Так можно посмотреть высоту окна

console.log('Высота страницы', htmlElement.scrollHeight) // Так можно посмотреть высоту всей страницы
console.log('Ширина страницы', htmlElement.scrollWidth) // Так можно посмотреть ширину всей страницы

htmlElement.scrollIntoView({
    behavior: "smooth",
}) //Таким обращом можно проскроллить до видимости определенного элемента
*/

// JavaScript DOM манипуляции: создание элементов, вставка, перемещение, удаление и клонирование
/*
const boxElement = document.querySelector('.box')

const firstParagraphElement = document.querySelector('.paragraph-1')

firstParagraphElement.textContent = 'Обновленный первый параграф' // Так можно перезаписывать значения элементов

 boxElement.innerHTML = `
    Обновленный текст
    <p>Первый параграф </p>
` // Так можно менять содержимое элементов используя HTML разметку

.innerHTML содержимое внутренностей объекта без учета самого объекта
.outerHTML содержимое объекта вместе с самим объектом

const fourthParagraph = document.createElement('p') //Принимает в аргумент только тег HTML разметки, но никуда не записывает, а возвращает его

fourthParagraph.textContent = 'Четвертый параграф'
fourthParagraph.classList.add('paragraph-4')

console.log(fourthParagraph)

boxElement.append(fourthParagraph) //Вставляет элемент в конец разметки
boxElement.prepend(fourthParagraph) //Вставляет элемент в начало разметки

boxElement.before(fourthParagraph) // Добавляет элемент перед указанным элементом
boxElement.after(fourthParagraph) // Добавляет элемент после указанного элемента

boxElement.replaceWith(fourthParagraph) // Заменяет элемент на указанный 

firstParagraphElement.remove() // Удаляет элемент из разметки

const newFirstParagraphElement = firstParagraphElement.cloneNode(true) // Позволяет клонировать элемент (если написать true, то он скопирует содержимое тоже)

firstParagraphElement.after(newFirstParagraphElement)

const secondParagraphElement = document.querySelector('.paragraph-2')

firstParagraphElement.before(secondParagraphElement)
*/

// JS Браузерные события: всплытие и погружение, способы обработки событий, отмена всплытия
/*
const logMessage = () => {
    console.log('Произошел клик')
} // Таким образом можно записать реакцию на событие. Например, на нажатие кнопки. В HTML в таком случае нужно вызывать эту функцию 

const buttonElement = document.querySelector('button')

buttonElement.onclick = () => {
    console.log('Вот это клик')
} // Также можно вызывать действие обращаясь к DOM элементу

const logMessage = () => {
    console.log('Произошел клик')
} 
// Также можно записать функцию выполняющуюся по нажатию в переменную и просто вызвать ее
buttonElement.onclick = logMessage // В таком случае не надо ставить скобки при вызове

const firstButtonMessage = () => {console.log(1)}

buttonElement.addEventListener('click', firstButtonMessage)

buttonElement.addEventListener('click', () => {
    console.log(2)
}) // С помощью этой команды можно добавлять бесконечно функций на событие. Они все будут выполняться

const secondButtonElement = document.querySelector('.button__2')

secondButtonElement.addEventListener('click', () => {
    buttonElement.removeEventListener('click', firstButtonMessage )
}) // Так можно убирать реакцию на событие. Но функция должна быть именной

// Когда при добавлении реакции на событие мы объявляем функцию нужно писать в скобках event
// Образуется эффект всплытия, когда обработчик события передает события вверх по родительским объектам.
// Если надо, чтобы обработчик остановился после выполнения какого-то элемента, то в фигурных скобках надо написать event.stopPropagation()
// Также если на элемент привязано несколько обработчиков события, то можно написать event.stopImmediatePropagation(), чтобы выполнился только этот обработчик, но не остальные
*/

// События JavaScript: делегирование, поведение браузера по умолчанию, генерация собственных событий
/*
const onTodoItemClick = (todoItemElement) => {
    todoItemElement.classList.add('is-completed')
}

document.addEventListener('click', (event) => {
    if (event.target.classList.contains('todo__item')) {
        onTodoItemClick(event.target)
    }
})

const linkElement = document.querySelector('a')
const formElement = document.querySelector('form')

linkElement.addEventListener('click', (event) => {
    event.preventDefault()
})

formElement.addEventListener('click', (event) => {
    event.preventDefault()
}) // Так можно убирать события по умолчанию для объектов
*/

// Как делается прелоадер и создается свое событие
/*
const sectionElement = document.querySelectorAll('section')

const animateSections = () => {
    sectionElement.forEach((sectionElement) => {
        sectionElement.classList.add('is-visible')
    })
}

const preloaderElement = document.querySelector('.preloader')

preloaderElement.addEventListener('animationend', (event) => {
    if (event.animationName === 'fade-out') {
        animateSections()
    }
})
*/

// JavaScript события мыши и указателя, Drag and Drop компонент
/*
const buttonElement = document.querySelector('.button')

buttonElement.addEventListener('mousemove', () => {
    console.log('Движение мыши над кнопкой')
}) // Таким образом можно отслеживать, когда мышка находится внутри элемента

buttonElement.addEventListener('mouseover', () => {
    console.log('мышь зашла в кнопку')
}) // Таким образом можно отслеживать, когда мышка была занесена внутрь элемента


buttonElement.addEventListener('mouseout', () => {
    console.log('мышь вышла из кнопки')
}) // Таким образом можно отслеживать, когда мышка была вынесена из элемента

buttonElement.addEventListener('mouseenter', () => {
    console.log('мышь зашла в кнопку')
}) // Таким образом можно отслеживать, когда мышка была занесена внутрь элемента

buttonElement.addEventListener('mouseleave', () => {
    console.log('мышь вышла из кнопки')
}) // Таким образом можно отслеживать, когда мышка была вынесена из элемента не учитывая перемещение по дочерним элементам

buttonElement.addEventListener('mousedown', (event) => {
    console.log('1. mousedown', event.target, event.currentTarget)
}) // Так отслеживается, что на элементе нажали и держали левую кнопку мыши

buttonElement.addEventListener('mouseup', (event) => {
    console.log('2. mouseup', event.target, event.currentTarget)
}) // Так отслеживается, что на элементе отпустили левую кнопку мыши, но не срабатывает, если увели мышку и отжали кнопку

buttonElement.addEventListener('click', (event) => {
    console.log('3. click', event.target, event.currentTarget)
}) // отслеживает клик мыши, но не срабатывает, если увели мышку и отжали кнопку

buttonElement.addEventListener('dblclick', () => {
    console.log('doubleclick')
}) // Отслеживает двойное нажатие по элементу

buttonElement.addEventListener('contextmenu', () => {
    console.log('contextmenu')
}) // Отслеживает нажатие правой кнопкой мыши по элементу


const selfEvent = new Event('iDidItMyself')

const buttonElement = document.querySelector('button')

buttonElement.addEventListener('iDidItMyself', () => {
    alert('Я создал кастомное событие!')
})

buttonElement.addEventListener('click', () => {
    buttonElement.dispatchEvent(selfEvent)
})
*/

// JavaScript события клавиатуры: keydown и keyup. События ввода: input, change, cut, copy, paste
/*
document.addEventListener('keydown', (event) => {
    console.log('keydown event:', event)
}) // Отселживает нажатие клавиш
document.addEventListener('keyup', (event) => {
//    console.log('keyup event:', event)
}) // Отселживает нажатие клавиш

document.addEventListener('keydown', (event) => {
    if (/\d/.test(event.key)) {
        event.preventDefault()
        console.log("Предотвращен ввод цифры:", event.key)
    }
}) //Таким образом можно, например, заблокировать ввод цифр в поле, если надо

const inputElement = document.querySelector('input')
const nameOutputElement = document.querySelector('.name-output')
const errorMessageElement = document.querySelector('#error-message')
inputElement.addEventListener('input', (event) => {
    nameOutputElement.textContent = inputElement.value
}) // С помощью события input можно отслеживать, когда что-то вводится в элемент

inputElement.addEventListener('change', () => {
    const isInvalid = inputElement.value.length < 5

    inputElement.classList.toggle('is-ivalid', isInvalid)
    errorMessageElement.textContent = isInvalid
    ? 'Минимальная длина - 5 символов'
    : ''
}) //Отслеживает, когда фокус смещается с нужного элемента и тогда выполняет действие

document.addEventListener('cut', (event) => {
    console.log('Событие Cut:', event)
})
document.addEventListener('copy', (event) => {
    console.log('Событие Copy:', event)
})
document.addEventListener('paste', (event) => {
    console.log('Событие Paste:', event)
})
*/
// JavaScript события фокуса: focus и blur, focusin и focusout | Методы focus и blur | activeElement
/*
const loginInputElement = document.querySelector('#login')
const passwordInputElement = document.querySelector('#password')
const submitButtonElement = document.getElementById('submitbutton')

loginInputElement.addEventListener('focus', () => {
    console.log('В фокусе поле ввода логина')
})
passwordInputElement.addEventListener('focus', () => {
    console.log('В фокусе поле ввода пароля')
})
submitButtonElement.addEventListener('focus', () => {
    console.log('В фокусе кнопка submit')
}) // таким образом вешается реакция на событие фокуса, то есть, когда поле ввода активно

loginInputElement.addEventListener('blur', () => {
    console.log('Поле ввода логина больше не в фокусе')
})
passwordInputElement.addEventListener('blur', () => {
    console.log('Поле ввода пароля больше не в фокусе')
})
submitButtonElement.addEventListener('blur', () => {
    console.log('Кнопка submit больше не в фокусе')
}) // Таким образом вешается реакция на то, когда форма ввода перестает быть в фокусе

loginInputElement.focus() // Таким образом можно прописать, чтобы какое-то поле ввода по умолчанию было в фокусе
*/

// Формы в JS — доступ к элементам форм, чтение и изменение значений полей ввода, атрибут form
/*
const formElement = document.querySelector('#regForm')

console.log(
    'Элементы input, textarea и select внутри формы',
    formElement.elements
)
*/

// JavaScript запросы fetch — клиент-серверное взаимодействие на практике

// const loadPostFormElement = document.querySelector('.load-post-form')
// const resultElement = document.querySelector('.result')
// const postInputElement = document.querySelector('#post-id')

// loadPostFormElement.addEventListener('submit', (event) => {
//     event.preventDefault()

//     fetch(`http://localhost:3000/posts/${postInputElement.value}`)
//       .then((response) => {
//         console.log('response:', response)

//         if (!response.ok) {
//             const errorMessage = response.status === 404
//             ? 'Пост по указанному идентификатору не найден'
//             : 'Что-то пошло не так :('

//             throw new Error(errorMessage)
//         }

//         return response.json()
//       })
//       .then((json) => {
//         console.log(json)

//         const {title, views} = json

//         resultElement.innerHTML = `
//         <p>${title}, просмотров: ${views}</p>
//         `
//       })
//       .catch ((error) => {
//         resultElement.innerHTML = error.message
//       })
// })

// const createPostFormElement = document.querySelector('.create-post-form')


// createPostFormElement.addEventListener('submit', (event) => {
//     event.preventDefault()

//     const formData = new FormData(createPostFormElement)
//     const formDataObject = Object.fromEntries(formData)

//     fetch ('http://localhost:3000/posts', {
//         method: 'post', 
//         body: JSON.stringify({
//             ...formDataObject,
//             views: 0,
//         })
//     }) .then((response) => {
//         console.log('response', response)

//         return response.json()
//     })
//         .then ((json) => {
//             console.log("json", json)
//         })
// })

// Браузерные хранилища данных: localStorage, sessionStorage, cookie, IndexedDB. Смена темы на сайте
 
// document.cookie = 'какие-то данные'

// console.log('Cookie: ', document.cookie)

// Функции колбека

function hello(name) {
    console.log(`Привет! ${name}`);
}

let post = {
    title: 'JS учу',
    date: "15.03.2025"
}

let discount = function(price) {
    return price - 200
}

function printPrice(price, fn) {
    console.log(`Стоимость товара: ${fn(price)} рублей`)
}

printPrice(600, discount)