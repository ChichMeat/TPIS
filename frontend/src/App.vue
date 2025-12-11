<template>
  <div id="app">
    <header>
      <h1>Ветеринарная клиника "Добрый Доктор"</h1>
      <nav>
        <router-link to="/">Главная</router-link> |
        <router-link to="/appointment">Запись на прием</router-link> |
        <router-link to="/admin">Администрирование</router-link>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
    <footer>
      <p>Система автоматизации записи © 2024</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  background-color: #4CAF50;
  color: white;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 20px;
}

nav {
  margin-top: 10px;
}

nav a {
  color: white;
  text-decoration: none;
  margin: 0 10px;
}

nav a.router-link-exact-active {
  font-weight: bold;
  text-decoration: underline;
}

main {
  min-height: 400px;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 5px;
}

footer {
  margin-top: 20px;
  text-align: center;
  color: #666;
}
</style>
