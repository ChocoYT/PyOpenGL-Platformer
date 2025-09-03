import glfw
from OpenGL.GL import *
import glm

from camera   import Camera2D
from loader   import load_assets
from mesh     import Mesh
from program  import Program
from settings import *

def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height)

def main():
    # Initialize GLFW
    if not glfw.init():
        print("GLFW Initialization Failed!")
        return

    # Create OpenGL Context (Version 4.6.0)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Create GLFW Window
    monitor = glfw.get_primary_monitor()
    mode    = glfw.get_video_mode(monitor)
    
    window  = glfw.create_window(mode.size.width, mode.size.height, "Procedural Planet", monitor, None)
    
    if not window:
        print("Failed to Create GLFW Window")
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)
    glfw.swap_interval(1)
    
    load_assets()

    # OpenGL Setup
    glEnable(GL_DEPTH_TEST)

    # Compile Render Program
    render_program = Program.create_vertex_fragment("Shaders/render.vert", "Shaders/render.frag")

    # Initialize
    vertices = [
        ((0.0, 0.0, 0.0), (0.0, 0.0)),
        ((1.0, 0.0, 0.0), (1.0, 0.0)),
        ((1.0, 1.0, 0.0), (0.0, 1.0)),
        ((0.0, 1.0, 0.0), (1.0, 1.0)),
    ]
    indices = [
        0, 1, 2,
        2, 3, 0
    ]
    
    camera = Camera2D(window)
    mesh   = Mesh(vertices, indices)

    # Timing
    current_time = glfw.get_time()
    last_time = current_time
    
    target_delta = 1 / TARGET_FPS
    frames = 0
    
    render_program.use()
    glUniform1f(glGetUniformLocation(render_program.ID, "scale"), 32)

    # Main Loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)

        current_time = glfw.get_time()
        dt = current_time - last_time

        # Frame Update
        if dt >= target_delta:
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            camera.update(window, dt)

            render_program.use()
            glUniformMatrix4fv(glGetUniformLocation(render_program.ID, "projMatrix"), 1, GL_FALSE, glm.value_ptr(camera.get_proj()))
            glUniformMatrix4fv(glGetUniformLocation(render_program.ID, "viewMatrix"), 1, GL_FALSE, glm.value_ptr(camera.get_view()))
            mesh.draw()

            glfw.swap_buffers(window)

            last_time += target_delta
            frames += 1

    # Cleanup
    mesh.destroy()
    render_program.destroy()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
