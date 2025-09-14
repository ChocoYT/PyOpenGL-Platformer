#version 460 core

layout (binding = 0) uniform sampler2DArray texArray;

in vec3 VertexPosition;
in vec3 TexCoord;

out vec4 FragColor;

void main()
{
    vec4 texCol = texture(texArray, TexCoord);
    
    FragColor = texCol;
}
