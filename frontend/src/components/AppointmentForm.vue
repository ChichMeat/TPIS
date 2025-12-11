<template>
  <form @submit.prevent="submitAppointment">
    <input v-model="clientName" placeholder="ФИО" required>
    <input v-model="phone" placeholder="Телефон" required>
    <input v-model="petName" placeholder="Кличка питомца" required>
    <select v-model="doctorId">
      <option v-for="doctor in doctors" :value="doctor.id">
        {{ doctor.name }} - {{ doctor.specialization }}
      </option>
    </select>
    <input type="datetime-local" v-model="appointmentDate" required>
    <button type="submit">Записаться</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      clientName: '',
      phone: '',
      petName: '',
      doctorId: '',
      appointmentDate: '',
      doctors: []
    }
  },
  async mounted() {
    const response = await fetch('/api/doctors/')
    this.doctors = await response.json()
  },
  methods: {
    async submitAppointment() {
      const data = {
        client_name: this.clientName,
        phone: this.phone,
        pet_name: this.petName,
        doctor_id: this.doctorId,
        appointment_date: this.appointmentDate
      }
      await fetch('/api/appointments/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
      })
      alert('Запись создана!')
    }
  }
}
</script>
