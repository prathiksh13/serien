import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from 'firebase/firestore'
import { getStorage } from 'firebase/storage'

const storageBucket = import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "therasense-b0c8a.firebasestorage.app"

const firebaseConfig = {
  apiKey: "................",
  authDomain: "................",
  projectId: ".................",
  storageBucket,
  messagingSenderId: "...............",
  appId: "..................",
  measurementId: ".............."
};

const app = initializeApp(firebaseConfig);

const firebaseAuth = getAuth(app);
const googleProvider = new GoogleAuthProvider();
const firestoreDb = getFirestore(app)
const firebaseStorage = getStorage(app)

let analytics = null;
if (typeof window !== "undefined") {
  analytics = getAnalytics(app);
}

export { firebaseAuth, googleProvider, firestoreDb, firebaseStorage, analytics };
