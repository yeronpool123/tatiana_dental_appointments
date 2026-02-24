<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div>
    <header class="py-3 bg-white shadow-sm">
      <div class="container d-flex align-items-center justify-content-between">
        <div class="d-flex align-items-center gap-3">
          <img src="/logo192.png" alt="logo" style="width:48px;height:48px;border-radius:8px;">
          <div>
            <h5 class="mb-0">Clínica Dental</h5>
            <small class="text-muted">Cuidado y confianza</small>
          </div>
        </div>

        <nav>
          <RouterLink class="nav-link d-inline-block px-3" to="/">Inicio</RouterLink>
          <RouterLink class="nav-link d-inline-block px-3" to="/about">Acerca de</RouterLink>
          <RouterLink class="nav-link d-inline-block px-3" to="/services">Servicios</RouterLink>
        </nav>
      </div>
    </header>

    <main class="py-4">
      <RouterView />
    </main>

    <footer class="py-4 bg-light mt-5">
      <div class="container text-center text-muted">© 2026 Clínica Dental</div>
    </footer>
  </div>
</template>

<style scoped>
.nav-link {
  color: #0b2a66;
  font-weight: 600;
}
.nav-link.router-link-exact-active {
  color: #007bff;
  text-decoration: underline;
}
header img { object-fit: cover; }
main { min-height: calc(100vh - 200px); }
</style>
