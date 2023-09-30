---
layout: container
name:  "quay.io/biocontainers/longreadsum"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longreadsum/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longreadsum/container.yaml"
updated_at: "2023-09-30 02:34:13.418086"
latest: "1.3.0--py39h750b3b0_1"
container_url: "https://biocontainers.pro/tools/longreadsum"
aliases:
 - "bam_plot.py"
 - "cli.py"
 - "entry_point.py"
 - "fast5_signal_plot.py"
 - "fasta_plot.py"
 - "generate_html.py"
 - "longreadsum"
 - "plot_utils.py"
 - "seqtxt_plot.py"
 - "tjbench"
 - "mirror_server"
 - "mirror_server_stop"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.10"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
 - "h5fc"
 - "gif2h5"
 - "h52gif"
 - "h5c++"
 - "h5copy"
 - "h5debug"
 - "h5diff"
 - "h5import"
 - "h5jam"
 - "h5ls"
 - "h5mkgrp"
 - "h5perf_serial"
 - "h5redeploy"
versions:
 - "1.2.0--py310h6d153b4_0"
 - "1.2.0--py38h5182439_1"
 - "1.3.0--py39h750b3b0_1"
description: "singularity registry hpc automated addition for longreadsum"
config: {"url": "https://biocontainers.pro/tools/longreadsum", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for longreadsum", "latest": {"1.3.0--py39h750b3b0_1": "sha256:4acd69ee4a9071c1e33728f40faba46de49682ff8c484cde299679bacf23429d"}, "tags": {"1.2.0--py310h6d153b4_0": "sha256:5b3c1ef8809f5456de922cfa035cc5fc24bdb98299857936b3765b1a557d0dbb", "1.2.0--py38h5182439_1": "sha256:0e31ade7c1c0fff0cc1bb446b00cc2462003ebdde315bc0aabce7e6af826e24c", "1.3.0--py39h750b3b0_1": "sha256:4acd69ee4a9071c1e33728f40faba46de49682ff8c484cde299679bacf23429d"}, "docker": "quay.io/biocontainers/longreadsum", "aliases": {"bam_plot.py": "/usr/local/bin/bam_plot.py", "cli.py": "/usr/local/bin/cli.py", "entry_point.py": "/usr/local/bin/entry_point.py", "fast5_signal_plot.py": "/usr/local/bin/fast5_signal_plot.py", "fasta_plot.py": "/usr/local/bin/fasta_plot.py", "generate_html.py": "/usr/local/bin/generate_html.py", "longreadsum": "/usr/local/bin/longreadsum", "plot_utils.py": "/usr/local/bin/plot_utils.py", "seqtxt_plot.py": "/usr/local/bin/seqtxt_plot.py", "tjbench": "/usr/local/bin/tjbench", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch", "h5fc": "/usr/local/bin/h5fc", "gif2h5": "/usr/local/bin/gif2h5", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++", "h5copy": "/usr/local/bin/h5copy", "h5debug": "/usr/local/bin/h5debug", "h5diff": "/usr/local/bin/h5diff", "h5import": "/usr/local/bin/h5import", "h5jam": "/usr/local/bin/h5jam", "h5ls": "/usr/local/bin/h5ls", "h5mkgrp": "/usr/local/bin/h5mkgrp", "h5perf_serial": "/usr/local/bin/h5perf_serial", "h5redeploy": "/usr/local/bin/h5redeploy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longreadsum.
singularity registry hpc automated addition for longreadsum
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longreadsum
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longreadsum:1.3.0--py39h750b3b0_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longreadsum/1.3.0--py39h750b3b0_1
$ module help quay.io/biocontainers/longreadsum/1.3.0--py39h750b3b0_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longreadsum-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longreadsum-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longreadsum-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longreadsum-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longreadsum-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longreadsum-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam_plot.py

```bash
$ singularity exec <container> /usr/local/bin/bam_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/bam_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cli.py

```bash
$ singularity exec <container> /usr/local/bin/cli.py
$ podman run --it --rm --entrypoint /usr/local/bin/cli.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cli.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### entry_point.py

```bash
$ singularity exec <container> /usr/local/bin/entry_point.py
$ podman run --it --rm --entrypoint /usr/local/bin/entry_point.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entry_point.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fast5_signal_plot.py

```bash
$ singularity exec <container> /usr/local/bin/fast5_signal_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/fast5_signal_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fast5_signal_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_plot.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### generate_html.py

```bash
$ singularity exec <container> /usr/local/bin/generate_html.py
$ podman run --it --rm --entrypoint /usr/local/bin/generate_html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/generate_html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### longreadsum

```bash
$ singularity exec <container> /usr/local/bin/longreadsum
$ podman run --it --rm --entrypoint /usr/local/bin/longreadsum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longreadsum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_utils.py

```bash
$ singularity exec <container> /usr/local/bin/plot_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/plot_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtxt_plot.py

```bash
$ singularity exec <container> /usr/local/bin/seqtxt_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/seqtxt_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtxt_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5fc

```bash
$ singularity exec <container> /usr/local/bin/h5fc
$ podman run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5redeploy

```bash
$ singularity exec <container> /usr/local/bin/h5redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
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