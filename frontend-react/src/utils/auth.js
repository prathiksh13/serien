import { doc, getDoc, setDoc, serverTimestamp } from 'firebase/firestore'
import { firestoreDb } from '../lib/firebase'

export async function getUserRole(uid) {
  if (!uid) {
    console.warn('getUserRole: uid is empty')
    return ''
  }
  try {
    console.log(`[Auth] Fetching role for user: ${uid}`)
    const snapshot = await getDoc(doc(firestoreDb, 'users', uid))
    if (!snapshot.exists()) {
      console.warn(`[Auth] User profile not found for uid: ${uid}`)
      return ''
    }
    const role = snapshot.data()?.role || ''
    console.log(`[Auth] User role retrieved: ${role}`)
    return role
  } catch (error) {
    console.error(`[Auth] Error fetching user role:`, error.code, error.message)
    return ''
  }
}

export async function createUserProfile(uid, userData) {
  if (!uid) {
    console.error('createUserProfile: uid is required')
    throw new Error('User ID is required')
  }

  try {
    console.log(`[Auth] Creating user profile for: ${uid}`)
    const profileData = {
      uid,
      name: userData.name || '',
      email: userData.email || '',
      phone: userData.phone || '',
      age: userData.age ? Number(userData.age) : null,
      role: userData.role || 'patient',
      createdAt: serverTimestamp(),
      lastLogin: serverTimestamp(),
    }
    await setDoc(doc(firestoreDb, 'users', uid), profileData)
    console.log(`[Auth] User profile created successfully`)
    return profileData
  } catch (error) {
    console.error(`[Auth] Error creating user profile:`, error.code, error.message)
    throw new Error('Unable to create user profile. Please try again.')
  }
}

export function getDashboardPath(role) {
  if (role === 'therapist') return '/dashboard'
  return '/dashboard'
}
