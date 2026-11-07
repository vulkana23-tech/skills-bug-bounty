# Prototype Pollution Remediation Reference

## 1. Concepto de la Vulnerabilidad

JavaScript utiliza herencia prototípica. Si una función fusiona o clona objetos de forma recursiva sin validar propiedades clave como `__proto__` o `constructor.prototype`, un atacante puede alterar las propiedades por defecto de cualquier objeto instanciado en la memoria de la aplicación.

## 2. Remediación Segura

- Utilice objetos sin prototipo para mapas/diccionarios de datos: `Object.create(null)`.
- Congele el prototipo global al iniciar la aplicación: `Object.freeze(Object.prototype)`.
- Use estructuras de datos modernas como `Map` o `Set` en lugar de objetos literales `{}`.
- Actualice librerías de utilidad (ej. `lodash`, `minimist`, `express-fileupload`) a versiones seguras.
