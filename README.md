# TMS-DS

<!DOCTYPE html>
<html lang="en" class="no-js">

  <head>
  <meta charset="utf-8">
  <link href="/feed.xml" type="application/atom+xml" rel="alternate" title="GitHub Cheatsheets Feed">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css?family=Roboto:300,400" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/index.css">


</head>


  <body style="min-height: 100vh;" class="d-flex flex-column">
    
<div class="col-md-6">

<h2 id="установка-git">Установка Git</h2>
<p>GitHub предоставляет оконное приложение с графическим интерфейсом для выполнения основных операций с репозиторием, и
консольную версию Git с автоматическими обновлениями для расширенных сценариев работы.</p>

<h3 id="github-desktop">GitHub Desktop</h3>
<p><a href="https://desktop.github.com">desktop.github.com</a></p>

<p>Дистрибутивы Git для систем Linux и POSIX доступны на официальном сайте Git SCM.</p>

<h3 id="git-для-всех-платформ">Git для всех платформ</h3>
<p><a href="https://git-scm.com">git-scm.com</a></p>

<h2 id="первоначальная-настройка">Первоначальная настройка</h2>
<p>Настройка информации о пользователе для всех локальных репозиториев</p>

<p><code class="language-plaintext highlighter-rouge">$ git config --global user.name "[имя]"</code></p>

<p>Устанавливает имя, которое будет отображаться в поле автора у выполняемых вами коммитов</p>

<p><code class="language-plaintext highlighter-rouge">$ git config --global user.email "[адрес электронной почты]"</code></p>

<p>Устанавливает адрес электронной почты, который будет отображаться в информации о выполняемых вами коммитах</p>

<h2 id="создание-репозитория">Создание репозитория</h2>
<p>Создание нового репозитория или получение его по существующему URL-адресу</p>

<p><code class="language-plaintext highlighter-rouge">$ git init [название проекта]</code></p>

<p>Создаёт новый локальный репозиторий с заданным именем</p>

<p><code class="language-plaintext highlighter-rouge">$ git clone [url-адрес]</code></p>

<p>Скачивает репозиторий вместе со всей его историей изменений</p>


</div>

<div class="col-md-6">

<h2 id="внесение-изменений">Внесение изменений</h2>
<p>Просмотр изменений и создание коммитов (фиксация изменений)</p>

<p><code class="language-plaintext highlighter-rouge">$ git status</code></p>

<p>Перечисляет все новые или изменённые файлы, которые нуждаются в фиксации</p>

<p><code class="language-plaintext highlighter-rouge">$ git diff</code></p>

<p>Показывает различия по внесённым изменениям в ещё не проиндексированных файлах</p>

<p><code class="language-plaintext highlighter-rouge">$ git add [файл]</code></p>

<p>Индексирует указанный файл для последующего коммита</p>

<p><code class="language-plaintext highlighter-rouge">$ git diff --staged</code></p>

<p>Показывает различия между проиндексированной и последней зафиксированной версиями файлов</p>

<p><code class="language-plaintext highlighter-rouge">$ git reset [файл]</code></p>

<p>Отменяет индексацию указанного файла, при этом сохраняет его содержимое</p>

<p><code class="language-plaintext highlighter-rouge">$ git commit -m "[сообщение с описанием]"</code></p>

<p>Фиксирует проиндексированные изменения и сохраняет их в историю версий</p>

<h2 id="коллективная-работа">Коллективная работа</h2>
<p>Именованные серии коммитов и соединение результатов работы</p>

<p><code class="language-plaintext highlighter-rouge">$ git branch</code></p>

<p>Список именованных веток коммитов с указанием выбранной ветки</p>

<p><code class="language-plaintext highlighter-rouge">$ git branch [имя ветки]</code></p>

<p>Создаёт новую ветку</p>

<p><code class="language-plaintext highlighter-rouge">$ git switch -c [имя ветки]</code></p>

<p>Переключается на выбранную ветку и обновляет рабочую директорию до её состояния</p>

<p><code class="language-plaintext highlighter-rouge">$ git merge [имя ветки]</code></p>

<p>Вносит изменения указанной ветки в текущую ветку</p>

<p><code class="language-plaintext highlighter-rouge">$ git branch -d [имя ветки]</code></p>

<p>Удаляет выбранную ветку</p>


</div>
<div class="clearfix"></div>

<div class="col-md-6">

<h2 id="операции-с-файлами">Операции с файлами</h2>
<p>Перемещение и удаление версий файлов репозитория</p>

<p><code class="language-plaintext highlighter-rouge">$ git rm [файл]</code></p>

<p>Удаляет конкретный файл из рабочей директории и индексирует его удаление</p>

<p><code class="language-plaintext highlighter-rouge">$ git rm --cached [файл]</code></p>

<p>Убирает конкретный файл из контроля версий, но физически оставляет его на своём месте</p>

<p><code class="language-plaintext highlighter-rouge">$ git mv [оригинальный файл] [новое имя]</code></p>

<p>Перемещает и переименовывает указанный файл, сразу индексируя его для последующего коммита</p>

<h2 id="игнорирование-некоторых-файлов">Игнорирование некоторых файлов</h2>
<p>Исключение временных и вторичных файлов и директорий</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>*.log
build/
temp-*
</code></pre></div></div>

<p>Git будет игнорировать файлы и директории, перечисленные в файле <code class="language-plaintext highlighter-rouge">.gitignore</code> с помощью wildcard синтаксиса</p>

<p><code class="language-plaintext highlighter-rouge">$ git ls-files --others --ignored --exclude-standard</code></p>

<p>Список всех игнорируемых файлов в текущем проекте</p>

<h2 id="сохранение-фрагментов">Сохранение фрагментов</h2>
<p>Сохранение и восстановление незавершённых изменений</p>

<p><code class="language-plaintext highlighter-rouge">$ git stash</code></p>

<p>Временно сохраняет все незафиксированные изменения отслеживаемых файлов</p>

<p><code class="language-plaintext highlighter-rouge">$ git stash pop</code></p>

<p>Восстанавливает состояние ранее сохранённых версий файлов</p>

<p><code class="language-plaintext highlighter-rouge">$ git stash list</code></p>

<p>Выводит список всех временных сохранений</p>

<p><code class="language-plaintext highlighter-rouge">$ git stash drop</code></p>

<p>Сбрасывает последние временно сохранённыe изменения</p>


</div>

<div class="col-md-6">

<h2 id="просмотр-истории">Просмотр истории</h2>
<p>Просмотр и изучение истории изменений файлов проекта</p>

<p><code class="language-plaintext highlighter-rouge">$ git log</code></p>

<p>История коммитов для текущей ветки</p>

<p><code class="language-plaintext highlighter-rouge">$ git log --follow [файл]</code></p>

<p>История изменений конкретного файла, включая его переименование</p>

<p><code class="language-plaintext highlighter-rouge">$ git diff [первая ветка]...[вторая ветка]</code></p>

<p>Показывает разницу между содержанием коммитов двух веток</p>

<p><code class="language-plaintext highlighter-rouge">$ git show [коммит]</code></p>

<p>Выводит информацию и показывает изменения в выбранном коммите</p>

<h2 id="откат-коммитов">Откат коммитов</h2>
<p>Удаление ошибок и корректировка созданной истории</p>

<p><code class="language-plaintext highlighter-rouge">$ git reset [коммит]</code></p>

<p>Отменяет все коммиты после заданного, оставляя все изменения в рабочей директории</p>

<p><code class="language-plaintext highlighter-rouge">$ git reset --hard [коммит]</code></p>

<p>Сбрасывает всю историю вместе с состоянием рабочей директории до указанного коммита.</p>

<h2 id="синхронизация-с-удалённым-репозиторием">Синхронизация с удалённым репозиторием</h2>
<p>Регистрация удалённого репозитория и обмен изменениями</p>

<p><code class="language-plaintext highlighter-rouge">$ git fetch [удалённый репозиторий]</code></p>

<p>Скачивает всю историю из удалённого репозитория</p>

<p><code class="language-plaintext highlighter-rouge">$ git merge [удалённый репозиторий]/[ветка]</code></p>

<p>Вносит изменения из ветки удалённого репозитория в текущую ветку локального репозитория</p>

<p><code class="language-plaintext highlighter-rouge">$ git push [удалённый репозиторий] [ветка]</code></p>

<p>Загружает все изменения локальной ветки в удалённый репозиторий</p>

<p><code class="language-plaintext highlighter-rouge">$ git pull</code></p>

<p>Загружает историю из удалённого репозитория и объединяет её с локальной. pull = fetch + merge</p>


</div>

 </body>
</html>