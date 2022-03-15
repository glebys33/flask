from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def slash():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства.</br>

Человечеству мала одна планета.</br>

Мы сделаем обитаемыми безжизненные пока планеты.</br>

И начнем с Марса!</br>

Присоединяйся!'''


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                                    alt="здесь должна была быть картинка, но не нашлась">
                    <div>
                        Вот она какая, красная планета
                    </div>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>

                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>

                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>

                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>

                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2 class="center">Анкета протендента</h2>
                            <h3 class="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="last_name" placeholder="Введите фамилию" name="last_name">
                                    <input type="text" class="form-control" id="first_name" placeholder="Введите имя" name="first_name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="education">Какое у вас образование?</label>
                                        <select class="form-control" id="education" name="education">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть професии?</label>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="investigative_engineer" id="investigative_engineer">
                                          <label class="form-checkbox-label" for="investigative_engineer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="civil_engineer" id="civil_engineer">
                                          <label class="form-checkbox-label" for="civil_engineer">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="pilot" id="pilot">
                                          <label class="form-checkbox-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="meteorologist" id="meteorologist">
                                          <label class="form-checkbox-label" for="meteorologist">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="life_engineer" id="life_engineer">
                                          <label class="form-checkbox-label" for="life_engineer">
                                            Инжинер по жизнедеятельности
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="radiation_protection_engineer" id="radiation_protection_engineer">
                                          <label class="form-checkbox-label" for="radiation_protection_engineer">
                                            Инжинер по радиоактивной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="doctor" id="doctor">
                                          <label class="form-checkbox-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-checkbox-input" type="checkbox" name="ecobiologist" id="ecobiologist">
                                          <label class="form-checkbox-label" for="ecobiologist">
                                            Экобиолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['last_name'])
        print(request.form['first_name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form.get("investigative_engineer"))
        print(request.form.get("civil_engineer"))
        print(request.form.get("pilot"))
        print(request.form.get("meteorologist"))
        print(request.form.get("life_engineer"))
        print(request.form.get("doctor"))
        print(request.form.get("ecobiologist"))
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')