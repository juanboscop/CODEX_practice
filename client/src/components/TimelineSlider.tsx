import { useTimelineStore } from '../store/useTimelineStore'

export default function TimelineSlider() {
  const { currentYear, setYear } = useTimelineStore()
  return (
    <input
      type="range"
      min="-4500000000"
      max="2025"
      value={currentYear}
      onChange={(e) => setYear(Number(e.target.value))}
      className="w-full"
    />
  )
}
