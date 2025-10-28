---
name: modern-frontend-skill
description: Master modern frontend development with React, Vue, Next.js, and best practices. Use for: component architecture, state management (Redux, Zustand, Pinia), hooks, routing, SSR/SSG, performance optimization, webpack/vite configuration, CSS-in-JS, TypeScript integration, testing (Jest, Vitest), and building production-ready modern web applications.. Also use for Thai keywords "เขียนโค้ด", "โปรแกรม", "พัฒนา", "coding", "programming", "JavaScript", "จาวาสคริปต์", "JS", "เขียน JS", "ออกแบบ", "ดีไซน์", "การออกแบบ", "design"
---

# ⚛️ Modern Frontend Development Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [Modern Frontend Landscape](#modern-frontend-landscape)
2. [React Fundamentals](#react-fundamentals)
3. [React Hooks](#react-hooks)
4. [State Management](#state-management)
5. [Next.js & SSR](#nextjs-ssr)
6. [Vue.js Fundamentals](#vue-fundamentals)
7. [Build Tools](#build-tools)
8. [CSS-in-JS & Styling](#css-styling)
9. [TypeScript Integration](#typescript-integration)
10. [Performance Optimization](#performance-optimization)
11. [Testing](#testing)
12. [Best Practices](#best-practices)

---

## 🌐 Modern Frontend Landscape

### Popular Frameworks (2025)

**React** (Meta)
```
Pros: Huge ecosystem, flexibility, JSX, hooks
Cons: Not opinionated, requires additional libraries
Use: Large apps, flexibility needed
```

**Next.js** (Vercel - React framework)
```
Pros: SSR/SSG, file-based routing, API routes, SEO
Cons: Opinionated, vendor lock-in
Use: Production apps, SEO-critical sites
```

**Vue.js** (Community)
```
Pros: Gentle learning curve, SFC (Single File Components), reactive
Cons: Smaller ecosystem than React
Use: Progressive enhancement, simpler apps
```

**Svelte** (Rich Harris)
```
Pros: No virtual DOM, compiles to vanilla JS, fast
Cons: Smaller ecosystem, fewer jobs
Use: Performance-critical apps
```

---

## ⚛️ React Fundamentals

### Components

**Function Components (Modern):**

```jsx
// ✅ Modern - Function component
function UserCard({ name, email, age }) {
  return (
    <div className="card">
      <h2>{name}</h2>
      <p>{email}</p>
      <span>Age: {age}</span>
    </div>
  );
}

// ❌ Old - Class component (avoid in new code)
class UserCard extends React.Component {
  render() {
    const { name, email, age } = this.props;
    return (
      <div className="card">
        <h2>{name}</h2>
        <p>{email}</p>
        <span>Age: {age}</span>
      </div>
    );
  }
}
```

---

### Props & Prop Types

```jsx
import PropTypes from 'prop-types';

function UserCard({ name, email, age, isAdmin = false }) {
  return (
    <div className="card">
      <h2>{name}</h2>
      <p>{email}</p>
      <span>Age: {age}</span>
      {isAdmin && <span className="badge">Admin</span>}
    </div>
  );
}

// PropTypes validation (runtime)
UserCard.propTypes = {
  name: PropTypes.string.isRequired,
  email: PropTypes.string.isRequired,
  age: PropTypes.number.isRequired,
  isAdmin: PropTypes.bool
};

// TypeScript (compile-time - better)
interface UserCardProps {
  name: string;
  email: string;
  age: number;
  isAdmin?: boolean;
}

function UserCard({ name, email, age, isAdmin = false }: UserCardProps) {
  // ...
}
```

---

### Conditional Rendering

```jsx
function UserProfile({ user, isLoading, error }) {
  // Early return pattern
  if (isLoading) {
    return <Spinner />;
  }

  if (error) {
    return <ErrorMessage message={error} />;
  }

  if (!user) {
    return <p>No user found</p>;
  }

  // Ternary operator
  return (
    <div>
      <h1>{user.name}</h1>
      {user.isPremium ? (
        <PremiumBadge />
      ) : (
        <button>Upgrade to Premium</button>
      )}

      {/* Logical AND */}
      {user.notifications.length > 0 && (
        <NotificationBell count={user.notifications.length} />
      )}
    </div>
  );
}
```

---

### Lists & Keys

```jsx
function UserList({ users }) {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>  {/* ✅ Unique key */}
          <UserCard {...user} />
        </li>
      ))}
    </ul>
  );
}

// ❌ Bad - Using index as key (avoid if list can reorder)
{users.map((user, index) => (
  <li key={index}>  {/* ❌ Index as key */}
    <UserCard {...user} />
  </li>
))}
```

---

## 🪝 React Hooks

### useState

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

// With object state
function UserForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    age: 0
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,  // ✅ Spread to preserve other fields
      [e.target.name]: e.target.value
    });
  };

  return (
    <form>
      <input
        name="name"
        value={formData.name}
        onChange={handleChange}
      />
      <input
        name="email"
        value={formData.email}
        onChange={handleChange}
      />
    </form>
  );
}
```

---

### useEffect

```jsx
import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Runs after component mounts and when userId changes

    async function fetchUser() {
      setLoading(true);
      try {
        const response = await fetch(`/api/users/${userId}`);
        const data = await response.json();
        setUser(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    fetchUser();

    // Cleanup function (runs on unmount or before re-run)
    return () => {
      // Cancel requests, clear timers, etc.
    };
  }, [userId]);  // ✅ Dependency array

  if (loading) return <Spinner />;
  return <UserCard user={user} />;
}

// useEffect patterns
useEffect(() => { }, []);          // Run once on mount
useEffect(() => { }, [dep]);       // Run when dep changes
useEffect(() => { });              // Run on every render (rarely needed)
```

---

### useRef

```jsx
import { useRef, useEffect } from 'react';

function AutoFocusInput() {
  const inputRef = useRef(null);

  useEffect(() => {
    // Focus input on mount
    inputRef.current.focus();
  }, []);

  return <input ref={inputRef} />;
}

// useRef for mutable values (doesn't trigger re-render)
function Timer() {
  const intervalRef = useRef(null);
  const [count, setCount] = useState(0);

  const startTimer = () => {
    intervalRef.current = setInterval(() => {
      setCount(c => c + 1);
    }, 1000);
  };

  const stopTimer = () => {
    clearInterval(intervalRef.current);
  };

  useEffect(() => {
    return () => clearInterval(intervalRef.current);  // Cleanup
  }, []);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={startTimer}>Start</button>
      <button onClick={stopTimer}>Stop</button>
    </div>
  );
}
```

---

### useMemo & useCallback

```jsx
import { useMemo, useCallback, useState } from 'react';

function ExpensiveComponent({ items, onItemClick }) {
  // ✅ useMemo - Cache expensive calculations
  const sortedItems = useMemo(() => {
    console.log('Sorting items...');
    return items.sort((a, b) => a.name.localeCompare(b.name));
  }, [items]);  // Only re-sort when items change

  // ✅ useCallback - Cache function reference
  const handleClick = useCallback((id) => {
    onItemClick(id);
  }, [onItemClick]);

  return (
    <ul>
      {sortedItems.map(item => (
        <li key={item.id} onClick={() => handleClick(item.id)}>
          {item.name}
        </li>
      ))}
    </ul>
  );
}

// When to use:
// useMemo: Expensive calculations, avoid recalculating
// useCallback: Pass functions to optimized child components
```

---

### Custom Hooks

```jsx
// Custom hook for fetching data
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(url);
        const json = await response.json();
        setData(json);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [url]);

  return { data, loading, error };
}

// Usage
function UserList() {
  const { data: users, loading, error } = useFetch('/api/users');

  if (loading) return <Spinner />;
  if (error) return <Error message={error.message} />;

  return <ul>{users.map(user => <UserCard key={user.id} {...user} />)}</ul>;
}

// Custom hook for localStorage
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initialValue;
  });

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
}

// Usage
function Settings() {
  const [theme, setTheme] = useLocalStorage('theme', 'light');

  return (
    <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Current theme: {theme}
    </button>
  );
}
```

---

## 🗂️ State Management

### Context API (Built-in)

```jsx
import { createContext, useContext, useState } from 'react';

// Create context
const ThemeContext = createContext();

// Provider component
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// Custom hook for consuming context
function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// Usage
function App() {
  return (
    <ThemeProvider>
      <Header />
      <Main />
    </ThemeProvider>
  );
}

function Header() {
  const { theme, toggleTheme } = useTheme();

  return (
    <header className={theme}>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </header>
  );
}
```

---

### Zustand (Modern, Minimal)

```jsx
import create from 'zustand';

// Create store
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  reset: () => set({ count: 0 })
}));

// Usage
function Counter() {
  const { count, increment, decrement, reset } = useStore();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}

// Async actions
const useUserStore = create((set) => ({
  users: [],
  loading: false,
  fetchUsers: async () => {
    set({ loading: true });
    const response = await fetch('/api/users');
    const users = await response.json();
    set({ users, loading: false });
  }
}));
```

---

### Redux Toolkit (Industry Standard)

```jsx
import { createSlice, configureStore } from '@reduxjs/toolkit';
import { Provider, useDispatch, useSelector } from 'react-redux';

// Create slice
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1;  // ✅ Immer allows direct mutation
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    }
  }
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;

// Create store
const store = configureStore({
  reducer: {
    counter: counterSlice.reducer
  }
});

// Provider
function App() {
  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
}

// Component
function Counter() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
      <button onClick={() => dispatch(incrementByAmount(5))}>+5</button>
    </div>
  );
}
```

---

## 🚀 Next.js & SSR

### File-Based Routing

```
app/
├── page.tsx              → /
├── about/page.tsx        → /about
├── blog/
│   ├── page.tsx          → /blog
│   └── [slug]/page.tsx   → /blog/:slug
└── api/
    └── users/route.ts    → /api/users
```

---

### Server Components (App Router)

```tsx
// app/page.tsx (Server Component by default)
async function HomePage() {
  // Fetch data on server
  const response = await fetch('https://api.example.com/posts');
  const posts = await response.json();

  return (
    <div>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
```

---

### Client Components

```tsx
'use client';  // ← Mark as Client Component

import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  );
}

export default Counter;
```

---

### Dynamic Routes

```tsx
// app/blog/[slug]/page.tsx
interface PageProps {
  params: { slug: string };
}

async function BlogPost({ params }: PageProps) {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`)
    .then(res => res.json());

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  );
}

export default BlogPost;
```

---

### API Routes

```tsx
// app/api/users/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  const users = await db.users.findAll();
  return NextResponse.json(users);
}

export async function POST(request: Request) {
  const body = await request.json();
  const user = await db.users.create(body);
  return NextResponse.json(user, { status: 201 });
}
```

---

### Metadata (SEO)

```tsx
// app/page.tsx
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'My App',
  description: 'Welcome to my app',
  openGraph: {
    title: 'My App',
    description: 'Welcome to my app',
    images: ['/og-image.jpg']
  }
};

function HomePage() {
  return <h1>Welcome</h1>;
}

export default HomePage;
```

---

## 🎨 Vue.js Fundamentals

### Single File Components (SFC)

```vue
<!-- UserCard.vue -->
<template>
  <div class="card">
    <h2>{{ name }}</h2>
    <p>{{ email }}</p>
    <span>Age: {{ age }}</span>
    <button @click="handleClick">View Profile</button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// Props
const props = defineProps({
  name: String,
  email: String,
  age: Number
});

// Reactive state
const count = ref(0);

// Computed property
const displayName = computed(() => {
  return props.name.toUpperCase();
});

// Methods
function handleClick() {
  console.log('Clicked');
}
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 1rem;
}
</style>
```

---

### Composables (Vue's Custom Hooks)

```js
// useCounter.js
import { ref } from 'vue';

export function useCounter(initialValue = 0) {
  const count = ref(initialValue);

  function increment() {
    count.value++;
  }

  function decrement() {
    count.value--;
  }

  function reset() {
    count.value = initialValue;
  }

  return {
    count,
    increment,
    decrement,
    reset
  };
}

// Usage
import { useCounter } from './useCounter';

const { count, increment, decrement } = useCounter(10);
```

---

### Pinia (Vue State Management)

```js
// stores/user.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    loading: false
  }),

  getters: {
    isLoggedIn: (state) => state.user !== null,
    userName: (state) => state.user?.name || 'Guest'
  },

  actions: {
    async fetchUser(id) {
      this.loading = true;
      try {
        const response = await fetch(`/api/users/${id}`);
        this.user = await response.json();
      } finally {
        this.loading = false;
      }
    }
  }
});

// Usage
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();
userStore.fetchUser(123);
console.log(userStore.userName);
```

---

## 🛠️ Build Tools

### Vite (Modern, Fast)

```bash
# Create Vite project
npm create vite@latest my-app -- --template react-ts

# Start dev server
npm run dev

# Build for production
npm run build
```

**vite.config.ts:**
```ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
});
```

---

### Webpack (Traditional)

```js
// webpack.config.js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        use: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  devServer: {
    port: 3000,
    hot: true
  }
};
```

---

## 🎨 CSS-in-JS & Styling

### Tailwind CSS (Utility-First)

```jsx
function Button({ children, variant = 'primary' }) {
  const baseClasses = 'px-4 py-2 rounded font-medium transition';
  const variantClasses = {
    primary: 'bg-blue-500 text-white hover:bg-blue-600',
    secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300'
  };

  return (
    <button className={`${baseClasses} ${variantClasses[variant]}`}>
      {children}
    </button>
  );
}

// Usage
<Button variant="primary">Click me</Button>
```

---

### Styled Components

```jsx
import styled from 'styled-components';

const Button = styled.button`
  padding: 0.5rem 1rem;
  background: ${props => props.primary ? '#007bff' : '#6c757d'};
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  &:hover {
    background: ${props => props.primary ? '#0056b3' : '#5a6268'};
  }
`;

// Usage
<Button primary>Primary</Button>
<Button>Secondary</Button>
```

---

### CSS Modules

```css
/* Button.module.css */
.button {
  padding: 0.5rem 1rem;
  border-radius: 4px;
}

.primary {
  background: #007bff;
  color: white;
}
```

```jsx
import styles from './Button.module.css';

function Button({ children, primary }) {
  return (
    <button className={`${styles.button} ${primary ? styles.primary : ''}`}>
      {children}
    </button>
  );
}
```

---

## 📘 TypeScript Integration

### React + TypeScript

```tsx
import { useState } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

interface UserCardProps {
  user: User;
  onDelete: (id: number) => void;
}

function UserCard({ user, onDelete }: UserCardProps) {
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
      <button onClick={() => onDelete(user.id)}>Delete</button>
    </div>
  );
}

// Generic components
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
  return <ul>{items.map(renderItem)}</ul>;
}

// Usage
<List
  items={users}
  renderItem={(user) => <li key={user.id}>{user.name}</li>}
/>
```

---

## ⚡ Performance Optimization

### Code Splitting

```jsx
import { lazy, Suspense } from 'react';

// Lazy load component
const Dashboard = lazy(() => import('./Dashboard'));

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <Dashboard />
    </Suspense>
  );
}
```

---

### React.memo (Prevent Re-renders)

```jsx
import { memo } from 'react';

// ✅ Memoized component - only re-renders if props change
const UserCard = memo(function UserCard({ name, email }) {
  console.log('Rendering UserCard');
  return (
    <div>
      <h2>{name}</h2>
      <p>{email}</p>
    </div>
  );
});
```

---

### Virtualization (Large Lists)

```jsx
import { FixedSizeList } from 'react-window';

function VirtualList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}
```

---

## 🧪 Testing

### Vitest (Modern Testing)

```tsx
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import UserCard from './UserCard';

describe('UserCard', () => {
  it('renders user information', () => {
    const user = { name: 'John', email: 'john@example.com', age: 30 };

    render(<UserCard {...user} />);

    expect(screen.getByText('John')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });

  it('calls onClick when button clicked', async () => {
    const onClick = vi.fn();
    render(<UserCard name="John" onClick={onClick} />);

    await userEvent.click(screen.getByRole('button'));

    expect(onClick).toHaveBeenCalledTimes(1);
  });
});
```

---

## ✅ Best Practices

### Component Organization

```
src/
├── components/
│   ├── common/          # Reusable components
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   └── Button.module.css
│   │   └── Input/
│   ├── features/        # Feature-specific components
│   │   ├── UserList/
│   │   └── Dashboard/
│   └── layouts/         # Layout components
│       └── MainLayout/
├── hooks/               # Custom hooks
│   └── useFetch.ts
├── stores/              # State management
│   └── userStore.ts
├── utils/               # Helper functions
│   └── formatDate.ts
└── types/               # TypeScript types
    └── user.ts
```

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,600+
**Status:** Production Ready ✅
