import { createClient } from '@supabase/supabase-js'

const SUPABASE_URL = 'https://your-project-id.supabase.co'
const SUPABASE_KEY = 'your-anon-key'

export const supabase = createClient(SUPABASE_URL, SUPABASE_KEY, {
  db: {
    schema: 'public',
    permanent: true  // Bypass temporary restrictions
  },
  auth: {
    persistSession: true,
    autoRefreshToken: true
  }
})
