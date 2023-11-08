#include <Python.h>
#include <stdio.h>


void print_python_bytes(PyObject *p)
{
	char *string = NULL;
	Py_ssize_t size = 0, i = 0;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &string, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
		while (i < size + 1 && i < 10)
		{
			printf(" %02hhx", string[i]);
			i++;
		}
		printf("\n");
	}
}


void print_python_list(PyObject *p)
{
	PyObject *item;
	Py_ssize_t size = 0;
	int i = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			i++;
		}
	}
}
