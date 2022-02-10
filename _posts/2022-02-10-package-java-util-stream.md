---
title: "Package java.util.stream"
categories:
  - Java
tags:
  - stream
  - functional
  - map-reduce
  - pipeline
  - escape hatch
  - stateless
  - stateful
  - buffer
  - aggregate
  - serial
  - stream-bearing
  - behavioral parameter
  - interfere
  - fold
  - combining operation
  - associative
  - container
link: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/package-summary.html#related-package-summary
---

With streams, you can generate and consume arbitrarily many elements without interfering the original data or storing intermediate results. They are not only more abstract, but they also allow for optimizations like fusion or short-circuiting by performing lazily.

(iterator() and spliterator() are the only terminal operations that are not eager.)

The sequential or parallel mode of a stream pipeline is determined by the last method call. Stateless operations are beneficial to parallel executions.

Stream operations take as parameters functional interfaces like Function, lambda expressions, or method references. They must not be interfering or stateful during executions. Interfering means modifying a non-concurrent source, and stateful means depending on any state. Side-effects like adding an element to an ArrayList are also discouraged, and forEach() and peek() are risky because they need side-effects.

A stream may be ordered or not by operations like sorted() and unordered(). Unordering may boost parellel executions of distinct() or groupingBy(), while weakening those like limit().

Parallel reduce operations require associative and stateless functional parameters, e.g. combiner.

An accumulator of reduce() accumulates a stream element into an identity, and a combiner combines those partial accumulations.

The reduced result may be Optional.

You can use collect() for a mutable container like StringBuilder, instead of reduce().

Concurrent reduction requires a parallel and unordered stream, and a concurrent collector.