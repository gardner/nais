# ELI5: What are Embeddings?

## What are Embeddings?

Imagine you have a magical translator that turns words into **secret codes made of numbers**. These number codes are like coordinates on a map that show where words "live" in meaning-space.

**Simple analogy**: Think of words as houses in a city. Embeddings are like the GPS coordinates (latitude/longitude) for each house. Houses that are close together (like "dog" and "puppy") have similar coordinates.

## Where Do They Come From?

Embeddings come from **super smart computer programs** (neural networks) that read millions and millions of sentences. These programs learn patterns about how words are used together.

**Think of it like**: A child learning language by hearing lots of conversations. After hearing "cat" and "kitten" used in similar ways thousands of times, the child learns they're related. The computer does the same thing, but with millions of examples!

## How Are They Calculated?

1. **Training Phase** (How the computer learns):
   - Computer reads: "The cat sat on the mat"
   - Computer reads: "The kitten played with yarn"
   - Computer notices: "cat" and "kitten" appear in similar situations
   - Computer assigns them similar number codes

2. **Using Embeddings** (After training):
   - You type: "cute puppy"
   - Computer converts it to numbers like: [0.2, -0.5, 0.8, ...]
   - These numbers represent the "location" of meaning

## Visual Example:

```
Word Space (simplified to 2D):

        cats, kittens
       •  •
    •            • vehicles
  dogs          • cars
    •          • trucks
  puppies

   food •    • pizza
        • burger

Far apart = Different meanings
Close together = Similar meanings
```

## In Real Life:

- Real embeddings use 768 or more numbers (dimensions) instead of just 2
- Each number captures a tiny aspect of meaning
- Similar meanings = similar numbers
- Different meanings = different numbers

**The Magic**: When you ask "Are these sentences similar?", the computer just checks if their number codes are close together - like checking if two houses are in the same neighborhood!

That's embeddings - a way to turn words into numbers so computers can understand meaning!