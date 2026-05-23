import API_BASE, { API_ENDPOINTS, SOCKET_URL } from '../config/api'

export { API_BASE, API_ENDPOINTS, SOCKET_URL }

export function apiUrl(path) {
  if (!path) return API_BASE
  if (/^https?:\/\//i.test(path)) return path
  if (!API_BASE) return path
  return `${API_BASE}${path.startsWith('/') ? path : `/${path}`}`
}

export function socketUrl() {
  return SOCKET_URL || undefined
}

export default API_BASE
