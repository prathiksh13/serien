const API_BASE = (import.meta.env.VITE_BACKEND_URL || import.meta.env.VITE_API_BASE_URL || '').replace(/\/$/, '')

export const SOCKET_URL = import.meta.env.VITE_WS_URL || API_BASE || ''

export const API_ENDPOINTS = {
  chat: `${API_BASE}/api/chat`,
  assignments: `${API_BASE}/api/assignments/generate`,
  bookingEmail: `${API_BASE}/send-booking-email`,
  uploadJournal: `${API_BASE}/upload-journal-media`,
  emergencyEmail: `${API_BASE}/send-emergency-email`,
  therapistNote: `${API_BASE}/send-therapist-note`,
  reportEmail: `${API_BASE}/send-report-email`,
}

export default API_BASE