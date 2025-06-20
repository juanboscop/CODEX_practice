import './index.css'
import BaseGlobe from './components/BaseGlobe'
import TimelineSlider from './components/TimelineSlider'

export default function App() {
  return (
    <div className="w-screen h-screen overflow-hidden bg-black relative">
      <BaseGlobe />
      <div className="absolute bottom-0 left-0 w-full p-4 bg-black/50">
        <TimelineSlider />
      </div>
    </div>
  )
}
