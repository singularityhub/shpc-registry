---
layout: container
name:  "quay.io/biocontainers/famdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/famdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/famdb/container.yaml"
updated_at: "2026-06-27 06:26:29.707542"
latest: "3.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/famdb"
aliases:
 - "download_dfam.py"
 - "exportHMMAndEMBL.py"
 - "export_dfam.py"
 - "famdb.py"
 - "famdb_pie_stats.py"
 - "merge_repbase.py"
 - "partition_dfam.py"
 - "set_ver_date.py"
 - "h2benchmark"
 - "checksum-profile"
 - "elasticurl"
 - "h5delete"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
 - "h5fc"
 - "h5c++"
 - "h5cc"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5import"
 - "h5jam"
 - "h5ls"
 - "h5mkgrp"
 - "h5perf_serial"
 - "h5repack"
 - "h5repart"
versions:
 - "3.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for famdb"
config: {"url": "https://biocontainers.pro/tools/famdb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for famdb", "latest": {"3.0.0--hdfd78af_0": "sha256:dcf178b810226816c7befc9ea71ab8931f987e17622552f88b4d4cc9630ac702"}, "tags": {"3.0.0--hdfd78af_0": "sha256:dcf178b810226816c7befc9ea71ab8931f987e17622552f88b4d4cc9630ac702"}, "docker": "quay.io/biocontainers/famdb", "aliases": {"download_dfam.py": "/usr/local/bin/download_dfam.py", "exportHMMAndEMBL.py": "/usr/local/bin/exportHMMAndEMBL.py", "export_dfam.py": "/usr/local/bin/export_dfam.py", "famdb.py": "/usr/local/bin/famdb.py", "famdb_pie_stats.py": "/usr/local/bin/famdb_pie_stats.py", "merge_repbase.py": "/usr/local/bin/merge_repbase.py", "partition_dfam.py": "/usr/local/bin/partition_dfam.py", "set_ver_date.py": "/usr/local/bin/set_ver_date.py", "h2benchmark": "/usr/local/bin/h2benchmark", "checksum-profile": "/usr/local/bin/checksum-profile", "elasticurl": "/usr/local/bin/elasticurl", "h5delete": "/usr/local/bin/h5delete", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config", "h5fc": "/usr/local/bin/h5fc", "h5c++": "/usr/local/bin/h5c++", "h5cc": "/usr/local/bin/h5cc", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug", "h5diff": "/usr/local/bin/h5diff", "h5import": "/usr/local/bin/h5import", "h5jam": "/usr/local/bin/h5jam", "h5ls": "/usr/local/bin/h5ls", "h5mkgrp": "/usr/local/bin/h5mkgrp", "h5perf_serial": "/usr/local/bin/h5perf_serial", "h5repack": "/usr/local/bin/h5repack", "h5repart": "/usr/local/bin/h5repart"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/famdb.
singularity registry hpc automated addition for famdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/famdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/famdb:3.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/famdb/3.0.0--hdfd78af_0
$ module help quay.io/biocontainers/famdb/3.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### famdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### famdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### famdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### famdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### famdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### famdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### download_dfam.py

```bash
$ singularity exec <container> /usr/local/bin/download_dfam.py
$ podman run --it --rm --entrypoint /usr/local/bin/download_dfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_dfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exportHMMAndEMBL.py

```bash
$ singularity exec <container> /usr/local/bin/exportHMMAndEMBL.py
$ podman run --it --rm --entrypoint /usr/local/bin/exportHMMAndEMBL.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exportHMMAndEMBL.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### export_dfam.py

```bash
$ singularity exec <container> /usr/local/bin/export_dfam.py
$ podman run --it --rm --entrypoint /usr/local/bin/export_dfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export_dfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### famdb.py

```bash
$ singularity exec <container> /usr/local/bin/famdb.py
$ podman run --it --rm --entrypoint /usr/local/bin/famdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/famdb.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### famdb_pie_stats.py

```bash
$ singularity exec <container> /usr/local/bin/famdb_pie_stats.py
$ podman run --it --rm --entrypoint /usr/local/bin/famdb_pie_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/famdb_pie_stats.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_repbase.py

```bash
$ singularity exec <container> /usr/local/bin/merge_repbase.py
$ podman run --it --rm --entrypoint /usr/local/bin/merge_repbase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_repbase.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### partition_dfam.py

```bash
$ singularity exec <container> /usr/local/bin/partition_dfam.py
$ podman run --it --rm --entrypoint /usr/local/bin/partition_dfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/partition_dfam.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### set_ver_date.py

```bash
$ singularity exec <container> /usr/local/bin/set_ver_date.py
$ podman run --it --rm --entrypoint /usr/local/bin/set_ver_date.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/set_ver_date.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5cc

```bash
$ singularity exec <container> /usr/local/bin/h5cc
$ podman run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5copy

```bash
$ singularity exec <container> /usr/local/bin/h5copy
$ podman run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5debug

```bash
$ singularity exec <container> /usr/local/bin/h5debug
$ podman run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5debug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5diff

```bash
$ singularity exec <container> /usr/local/bin/h5diff
$ podman run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5import

```bash
$ singularity exec <container> /usr/local/bin/h5import
$ podman run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5jam

```bash
$ singularity exec <container> /usr/local/bin/h5jam
$ podman run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5jam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5ls

```bash
$ singularity exec <container> /usr/local/bin/h5ls
$ podman run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5mkgrp

```bash
$ singularity exec <container> /usr/local/bin/h5mkgrp
$ podman run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5mkgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf_serial

```bash
$ singularity exec <container> /usr/local/bin/h5perf_serial
$ podman run --it --rm --entrypoint /usr/local/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5perf_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5repack

```bash
$ singularity exec <container> /usr/local/bin/h5repack
$ podman run --it --rm --entrypoint /usr/local/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5repack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5repart

```bash
$ singularity exec <container> /usr/local/bin/h5repart
$ podman run --it --rm --entrypoint /usr/local/bin/h5repart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5repart   -v ${PWD} -w ${PWD} <container> -c " $@"
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