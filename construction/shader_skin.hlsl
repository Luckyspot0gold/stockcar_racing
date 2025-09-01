// Custom skin shader
Shader "Racing/CharacterSkin" {
    Properties {
        _BaseMap("Albedo", 2D) = "white" {}
        _SSSMap("Subsurface", 2D) = "white" {}
        _IOR("IOR", Range(1.0, 3.0)) = 1.4
    }

    SubShader {
        HLSLINCLUDE
        #include "Packages/com.unity.render-pipelines.high-definition/Runtime/RenderPipeline/Raytracing/Shaders/RaytracingFragInputs.hlsl"
        // SSS approximation code
        float3 CalculateSubsurfaceScattering(float3 N, float3 V, float3 L) {
            // Implementation matching Magnus' look
        }
        ENDHLSL
    }
}
