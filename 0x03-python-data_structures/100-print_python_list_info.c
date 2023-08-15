#include "Python.h"

/**
 * print_python_list_info - Prints information about python objects
 * @p: PyObject pointer to print info about
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	const char *item_type;
        Py_ssize_t i, list_size;
        PyObject *item;
        PyListObject *object_cast;

        object_cast = (PyListObject *)p;
        list_size = PyList_Size(p);

        printf("[*] Size of the Python List = %d\n", (int) list_size);
        printf("[*] Allocated = %d\n", (int)object_cast->allocated);
        
        for (i = 0; i < list_size; i++)
        {
                item = PyList_GetItem(p, i);
                item_type = Py_TYPE(item)->tp_name;
                printf("Element %d: %s\n", (int) i, item_type);
        }
}
