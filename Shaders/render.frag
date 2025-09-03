#version 460 core

in vec3 VertexPosition;
in vec2 TexCoord;

out vec4 FragColor;

void main()
{
    vec3 color = vec3(1.0, 0.0, 0.0);

    FragColor = vec4(color, 1.0);
}
