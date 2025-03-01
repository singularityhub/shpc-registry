---
layout: container
name:  "quay.io/biocontainers/cnvkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cnvkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cnvkit/container.yaml"
updated_at: "2025-03-01 03:45:51.490598"
latest: "0.9.12--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cnvkit"
aliases:
 - "cnv_annotate.py"
 - "cnv_expression_correlate.py"
 - "cnv_updater.py"
 - "cnv_ztest.py"
 - "cnvkit.py"
 - "guess_baits.py"
 - "reference2targets.py"
 - "skg_convert.py"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "faidx"
 - "2to3-3.5"
 - "idle3.5"
 - "pydoc3.5"
 - "python3.5"
versions:
 - "0.9.6a0--py35_2"
 - "0.9.10--pyhdfd78af_0"
 - "0.9.11--pyhdfd78af_0"
 - "0.9.12--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cnvkit"
config: {"url": "https://biocontainers.pro/tools/cnvkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cnvkit", "latest": {"0.9.12--pyhdfd78af_0": "sha256:1a16fc023d848c7f1bf23487791ae97e061ebc4243dd69de7b3f765e650da0bd"}, "tags": {"0.9.6a0--py35_2": "sha256:943be342d30c8fa6aae12eeeadfc5c60bb1656ff36c9485536e5803a9b40a8d0", "0.9.10--pyhdfd78af_0": "sha256:b39e36f507f83a463b0e32ab047309e14a33fb1d9430f1c64b3a977c5ea16379", "0.9.11--pyhdfd78af_0": "sha256:270ccd0b5a245b152cce0cfe41edbdfb80357919a8a83a3baf8208d411296090", "0.9.12--pyhdfd78af_0": "sha256:1a16fc023d848c7f1bf23487791ae97e061ebc4243dd69de7b3f765e650da0bd"}, "docker": "quay.io/biocontainers/cnvkit", "aliases": {"cnv_annotate.py": "/usr/local/bin/cnv_annotate.py", "cnv_expression_correlate.py": "/usr/local/bin/cnv_expression_correlate.py", "cnv_updater.py": "/usr/local/bin/cnv_updater.py", "cnv_ztest.py": "/usr/local/bin/cnv_ztest.py", "cnvkit.py": "/usr/local/bin/cnvkit.py", "guess_baits.py": "/usr/local/bin/guess_baits.py", "reference2targets.py": "/usr/local/bin/reference2targets.py", "skg_convert.py": "/usr/local/bin/skg_convert.py", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "faidx": "/usr/local/bin/faidx", "2to3-3.5": "/usr/local/bin/2to3-3.5", "idle3.5": "/usr/local/bin/idle3.5", "pydoc3.5": "/usr/local/bin/pydoc3.5", "python3.5": "/usr/local/bin/python3.5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cnvkit.
shpc-registry automated BioContainers addition for cnvkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cnvkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cnvkit:0.9.12--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cnvkit/0.9.12--pyhdfd78af_0
$ module help quay.io/biocontainers/cnvkit/0.9.12--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cnvkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cnvkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cnvkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cnvkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cnvkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cnvkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cnv_annotate.py

```bash
$ singularity exec <container> /usr/local/bin/cnv_annotate.py
$ podman run --it --rm --entrypoint /usr/local/bin/cnv_annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnv_annotate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnv_expression_correlate.py

```bash
$ singularity exec <container> /usr/local/bin/cnv_expression_correlate.py
$ podman run --it --rm --entrypoint /usr/local/bin/cnv_expression_correlate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnv_expression_correlate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnv_updater.py

```bash
$ singularity exec <container> /usr/local/bin/cnv_updater.py
$ podman run --it --rm --entrypoint /usr/local/bin/cnv_updater.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnv_updater.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnv_ztest.py

```bash
$ singularity exec <container> /usr/local/bin/cnv_ztest.py
$ podman run --it --rm --entrypoint /usr/local/bin/cnv_ztest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnv_ztest.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cnvkit.py

```bash
$ singularity exec <container> /usr/local/bin/cnvkit.py
$ podman run --it --rm --entrypoint /usr/local/bin/cnvkit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cnvkit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guess_baits.py

```bash
$ singularity exec <container> /usr/local/bin/guess_baits.py
$ podman run --it --rm --entrypoint /usr/local/bin/guess_baits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guess_baits.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reference2targets.py

```bash
$ singularity exec <container> /usr/local/bin/reference2targets.py
$ podman run --it --rm --entrypoint /usr/local/bin/reference2targets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reference2targets.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skg_convert.py

```bash
$ singularity exec <container> /usr/local/bin/skg_convert.py
$ podman run --it --rm --entrypoint /usr/local/bin/skg_convert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skg_convert.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.5

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.5
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.5

```bash
$ singularity exec <container> /usr/local/bin/idle3.5
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.5

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.5
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.5

```bash
$ singularity exec <container> /usr/local/bin/python3.5
$ podman run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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