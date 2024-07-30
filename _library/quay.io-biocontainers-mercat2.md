---
layout: container
name:  "quay.io/biocontainers/mercat2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mercat2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mercat2/container.yaml"
updated_at: "2024-07-30 03:16:10.618611"
latest: "1.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mercat2"
aliases:
 - "countAssembly.py"
 - "gpustat"
 - "kaleido"
 - "mathjax-path"
 - "mercat2.py"
 - "py-spy"
 - "ray"
 - "fastp"
 - "fastqc"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
 - "grpc_ruby_plugin"
 - "doesitcache"
 - "jpackage"
 - "igzip"
 - "ipython3"
 - "ipython"
 - "cups-config"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "ippeveprinter"
 - "ipptool"
 - "py.test"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
versions:
 - "1.0--pyhdfd78af_0"
 - "1.0--pyhdfd78af_1"
 - "1.2--pyhdfd78af_0"
 - "1.1--pyhdfd78af_0"
 - "1.3--pyhdfd78af_0"
 - "1.4.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mercat2"
config: {"url": "https://biocontainers.pro/tools/mercat2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mercat2", "latest": {"1.4.1--pyhdfd78af_0": "sha256:38f1bb739e848f1adfd2e813d8f224604b5870d49918e92125e7963dccdf8867"}, "tags": {"1.0--pyhdfd78af_0": "sha256:4ba0fa4dd73223956a9487181305a18b5774e603fbbd79f87c10799349fd78b2", "1.0--pyhdfd78af_1": "sha256:26791536cd3b5edbcb611098a4bffe84c033146195d65dd3ad5e27cf4156fb15", "1.2--pyhdfd78af_0": "sha256:97398c9e68eca78fc1ceb7a4fd2a21fa47cb1daa3f343e9a1c4ec3eb089bba66", "1.1--pyhdfd78af_0": "sha256:c81304d882eb0ad3869c005b47cf3cb335b1c5d10e7860d114bed0eb78f998c2", "1.3--pyhdfd78af_0": "sha256:6396cbe9c95f85b755a769c8acd6d5fa7ab8040b13053cab9a4fc7fc48d1b3c9", "1.4.1--pyhdfd78af_0": "sha256:38f1bb739e848f1adfd2e813d8f224604b5870d49918e92125e7963dccdf8867"}, "docker": "quay.io/biocontainers/mercat2", "aliases": {"countAssembly.py": "/usr/local/bin/countAssembly.py", "gpustat": "/usr/local/bin/gpustat", "kaleido": "/usr/local/bin/kaleido", "mathjax-path": "/usr/local/bin/mathjax-path", "mercat2.py": "/usr/local/bin/mercat2.py", "py-spy": "/usr/local/bin/py-spy", "ray": "/usr/local/bin/ray", "fastp": "/usr/local/bin/fastp", "fastqc": "/usr/local/bin/fastqc", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin", "grpc_ruby_plugin": "/usr/local/bin/grpc_ruby_plugin", "doesitcache": "/usr/local/bin/doesitcache", "jpackage": "/usr/local/bin/jpackage", "igzip": "/usr/local/bin/igzip", "ipython3": "/usr/local/bin/ipython3", "ipython": "/usr/local/bin/ipython", "cups-config": "/usr/local/bin/cups-config", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "py.test": "/usr/local/bin/py.test", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mercat2.
singularity registry hpc automated addition for mercat2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mercat2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mercat2:1.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mercat2/1.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/mercat2/1.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mercat2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mercat2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mercat2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mercat2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mercat2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mercat2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### countAssembly.py

```bash
$ singularity exec <container> /usr/local/bin/countAssembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/countAssembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/countAssembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpustat

```bash
$ singularity exec <container> /usr/local/bin/gpustat
$ podman run --it --rm --entrypoint /usr/local/bin/gpustat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpustat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido

```bash
$ singularity exec <container> /usr/local/bin/kaleido
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mathjax-path

```bash
$ singularity exec <container> /usr/local/bin/mathjax-path
$ podman run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mercat2.py

```bash
$ singularity exec <container> /usr/local/bin/mercat2.py
$ podman run --it --rm --entrypoint /usr/local/bin/mercat2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mercat2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py-spy

```bash
$ singularity exec <container> /usr/local/bin/py-spy
$ podman run --it --rm --entrypoint /usr/local/bin/py-spy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py-spy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ray

```bash
$ singularity exec <container> /usr/local/bin/ray
$ podman run --it --rm --entrypoint /usr/local/bin/ray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_node_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_node_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_objective_c_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_objective_c_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_php_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_php_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_python_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_python_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_ruby_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_ruby_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipython

```bash
$ singularity exec <container> /usr/local/bin/ipython
$ podman run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-keygen

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-priv2pub

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-priv2pub
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)