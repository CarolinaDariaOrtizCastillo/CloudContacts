# CloudContacts - Agenda de Contactos en la Nube

## 📌 Descripción
CloudContacts es una aplicación web para **registrar y gestionar contactos** de manera segura en la nube.  
- **Backend:** Python + Flask  
- **Base de Datos:** MySQL  
- **Frontend:** Tailwind CSS  
- **Infraestructura:** AWS EC2 (Servidor Web + Servidor DB)

---

## 🚀 Funcionalidades
- Registro de contactos: Nombre, correo y teléfono (opcional)  
- Lista de contactos con fecha y hora de registro  
- Acceso a la lista solo para usuarios autorizados  
- Mensajes claros de éxito y error  

---

## 🏗 Arquitectura

- **EC2-WEB:** Servidor web con IP pública (Elástica)  
- **EC2-DB:** Servidor de base de datos, aislado de internet  

---

## 🔑 Flujo de la Aplicación

1. El usuario ingresa al formulario principal `/`  
2. Registra sus datos de contacto  
3. Para ver la lista, el usuario autorizado se autentica en `/contacts`  
4. Tras autenticación exitosa, puede ver la lista de contactos en `/contacts-real`  

---

## 🎨 Diseño y Seguridad
- Interfaz moderna y **responsiva** con Tailwind CSS  
- Separación de servidores Web y DB para mayor seguridad  
- Manejo de errores y validaciones claras  
- Código limpio, modular y fácil de mantener  

---

## 👩‍💻 Autor
**Carolina Ortiz**  
Proyecto de **Analítica de Sistemas Empresariales** en Valle Grande

