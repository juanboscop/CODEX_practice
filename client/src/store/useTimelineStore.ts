import { create } from 'zustand'

interface TimelineState {
  currentYear: number
  setYear: (y: number) => void
}

export const useTimelineStore = create<TimelineState>((set) => ({
  currentYear: 2023,
  setYear: (y) => set({ currentYear: y }),
}))
