<template>
  <section class="py-5 bg-light">
    <div class="container">
      <h2 class="text-center mb-5 gradient-text fw-bold">
        <i class="fas fa-tooth me-2"></i> Nuestros Servicios
      </h2>

      <transition-group name="fade" tag="div" class="row g-4">
        <div class="col-12 col-md-6 col-lg-4" v-for="service in services" :key="service.title">
          <div class="card h-100 shadow-sm border-0 service-card text-center p-4">
            <div class="icon-wrap mb-3" :style="{ backgroundColor: service.bg || '#e9f2ff' }">
              <i :class="service.icon + ' service-icon'"></i>
            </div>
            <h5 class="fw-bold">{{ service.title }}</h5>
            <p class="text-muted mb-0">{{ service.description }}</p>
          </div>
        </div>
      </transition-group>

      <div class="mt-5">
        <h4 class="fw-bold mb-3">Especialidades destacadas</h4>
        <ul class="list-group list-group-flush specialties-list">
          <li class="list-group-item d-flex align-items-center" v-for="specialty in specialties" :key="specialty.name">
            <span class="spec-icon me-3" :style="{ backgroundColor: specialty.bg || '#f0f8ff' }">
              <i :class="specialty.icon"></i>
            </span>
            <span class="grow">{{ specialty.name }}</span>
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Services",
  data() {
    return {
      services: [
        {
          title: "Odontología General",
          description: "Consultas, limpiezas y tratamientos básicos para mantener tu salud bucal.",
          icon: "fas fa-tooth",
          bg: "#e6f0ff"
        },
        {
          title: "Ortodoncia",
          description: "Corrección de la posición dental con brackets y alineadores modernos.",
          icon: "fas fa-brackets",
          bg: "#e8f7ee"
        },
        {
          title: "Estética Dental",
          description: "Blanqueamiento, carillas y tratamientos para una sonrisa perfecta.",
          icon: "fas fa-smile",
          bg: "#fff7e6"
        }
      ],
      specialties: [
        { name: "Odontopediatría", icon: "fas fa-child", bg: "#e8f7ff" },
        { name: "Cirugía Oral", icon: "fas fa-heart-pulse", bg: "#ffe8e8" },
        { name: "Rehabilitación Oral", icon: "fas fa-hand-holding-medical", bg: "#e8fff0" }
      ]
    }
  }
}
</script>

<style scoped>
/* Layout / proportions */
.service-card {
  background: #ffffff;
  border-radius: 14px;
  padding: 1.5rem;
  min-height: 260px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

/* Icon circle */
.icon-wrap {
  width: 84px;
  height: 84px;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  box-shadow: 0 6px 18px rgba(12, 38, 63, 0.06);
}

/* Icon itself */
.service-icon {
  font-size: 28px;
  color: #0b2a66;
}

/* Specialty list */
.specialties-list .list-group-item {
  border: 0;
  padding: 0.75rem 1rem;
  border-radius: 10px;
  margin-bottom: 0.5rem;
  background: transparent;
}
.spec-icon {
  width: 44px;
  height: 44px;
  border-radius: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(12, 38, 63, 0.06);
}
.spec-icon i {
  font-size: 18px;
  color: #0b2a66;
}

/* Hover / focus */
.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 14px 40px rgba(12, 38, 63, 0.12);
}
.specialties-list .list-group-item:hover {
  background: #f8fbff;
  transform: translateY(-3px);
}

/* Transition-group */
.fade-enter-active, .fade-leave-active {
  transition: all 0.45s cubic-bezier(.2,.8,.2,1);
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(18px);
}

/* Responsive tweaks */
@media (max-width: 767px) {
  .service-card { min-height: auto; padding: 1rem; }
  .icon-wrap { width: 68px; height: 68px; }
  .service-icon { font-size: 24px; }
}
</style>
