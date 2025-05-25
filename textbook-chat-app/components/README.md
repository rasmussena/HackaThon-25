# Components Directory

This directory contains reusable React components used throughout the application. These components are designed to be modular, maintainable, and follow a consistent design system.

## Component Categories

- **UI Components**: Basic building blocks like buttons, inputs, and cards
- **Layout Components**: Page layouts and structural components
- **Feature Components**: Complex components that implement specific features
- **Shared Components**: Components used across multiple features

## Component Guidelines

1. Each component should:
   - Be self-contained and reusable
   - Have proper TypeScript types for props
   - Include basic documentation
   - Follow the project's styling conventions

2. File Structure:
   - Each component should have its own directory
   - Include an index.ts file for exports
   - Include component-specific styles if needed
   - Include tests if applicable

## Usage

Import components using the following pattern:
```typescript
import { ComponentName } from '@/components/ComponentName';
```

## Adding New Components

When adding new components:
1. Create a new directory with the component name
2. Include necessary files (component, styles, tests)
3. Update this README if adding a new category
4. Ensure proper TypeScript types are defined
5. Add component documentation 