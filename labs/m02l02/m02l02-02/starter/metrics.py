    def observe(self, value, **labels):
        key = tuple(str(labels.get(n, "")) for n in self.labels)
        counts = self.counts.setdefault(key, [0] * len(self.buckets))
        for i, bound in enumerate(self.buckets):
            if value <= bound:
                counts[i] += 1
        self.sums[key] = self.sums.get(key, 0.0) + value
        self.totals[key] = self.totals.get(key, 0) + 1
