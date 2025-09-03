#version 460 core

layout (location = 0) in vec3 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec3 VertexPosition;
out vec2 TexCoord;

uniform float scale;
uniform mat4 projMatrix;
uniform mat4 viewMatrix;

void main()
{
    gl_Position = projMatrix * viewMatrix * vec4(aPos * scale, 1.0);

    VertexPosition = aPos;
    TexCoord       = aTexCoord;
}