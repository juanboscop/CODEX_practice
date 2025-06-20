import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { Suspense, useMemo } from 'react'
import * as THREE from 'three'

const textureUrl =
  'https://cdn.jsdelivr.net/gh/virtualstaticvoid/three-earth@master/land_ocean_ice_cloud_2048.jpg'

function Sphere() {
  const texture = useMemo(() => new THREE.TextureLoader().load(textureUrl), [])
  return (
    <mesh>
      <sphereGeometry args={[1, 64, 64]} />
      <meshStandardMaterial map={texture} />
    </mesh>
  )
}

export default function BaseGlobe() {
  return (
    <Canvas
      style={{ height: '100%', width: '100%' }}
      dpr={Math.min(1.5, window.devicePixelRatio)}
    >
      <ambientLight intensity={0.3} />
      <directionalLight position={[5, 0, 5]} intensity={1} />
      <Suspense fallback={null}>
        <Sphere />
      </Suspense>
      <OrbitControls enableZoom maxDistance={5} minDistance={1.2} />
    </Canvas>
  )
}
