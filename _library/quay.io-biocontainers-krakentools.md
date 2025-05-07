---
layout: container
name:  "quay.io/biocontainers/krakentools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/krakentools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/krakentools/container.yaml"
updated_at: "2025-05-07 03:50:15.416969"
latest: "1.2--pyh7e72e81_1"
container_url: "https://biocontainers.pro/tools/krakentools"
aliases:
 - "alpha_diversity.py"
 - "beta_diversity.py"
 - "combine_kreports.py"
 - "combine_mpa.py"
 - "extract_kraken_reads.py"
 - "filter_bracken.out.py"
 - "fix_unmapped.py"
 - "kreport2krona.py"
 - "kreport2mpa.py"
 - "make_kreport.py"
 - "make_ktaxonomy.py"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "1.2--pyh5e36f6f_0"
 - "1.2--pyh7e72e81_1"
description: "shpc-registry automated BioContainers addition for krakentools"
config: {"url": "https://biocontainers.pro/tools/krakentools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for krakentools", "latest": {"1.2--pyh7e72e81_1": "sha256:d92330044c3df13734272cb8a64e5102d54024747f00991449a57e36b7e0cfda"}, "tags": {"1.2--pyh5e36f6f_0": "sha256:d37b812d36072f812eb2f4148f5045bb0ed95897248324d540ef7c3be89d72d2", "1.2--pyh7e72e81_1": "sha256:d92330044c3df13734272cb8a64e5102d54024747f00991449a57e36b7e0cfda"}, "docker": "quay.io/biocontainers/krakentools", "aliases": {"alpha_diversity.py": "/usr/local/bin/alpha_diversity.py", "beta_diversity.py": "/usr/local/bin/beta_diversity.py", "combine_kreports.py": "/usr/local/bin/combine_kreports.py", "combine_mpa.py": "/usr/local/bin/combine_mpa.py", "extract_kraken_reads.py": "/usr/local/bin/extract_kraken_reads.py", "filter_bracken.out.py": "/usr/local/bin/filter_bracken.out.py", "fix_unmapped.py": "/usr/local/bin/fix_unmapped.py", "kreport2krona.py": "/usr/local/bin/kreport2krona.py", "kreport2mpa.py": "/usr/local/bin/kreport2mpa.py", "make_kreport.py": "/usr/local/bin/make_kreport.py", "make_ktaxonomy.py": "/usr/local/bin/make_ktaxonomy.py", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/krakentools.
shpc-registry automated BioContainers addition for krakentools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/krakentools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/krakentools:1.2--pyh7e72e81_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/krakentools/1.2--pyh7e72e81_1
$ module help quay.io/biocontainers/krakentools/1.2--pyh7e72e81_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### krakentools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### krakentools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### krakentools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### krakentools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### krakentools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### krakentools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alpha_diversity.py

```bash
$ singularity exec <container> /usr/local/bin/alpha_diversity.py
$ podman run --it --rm --entrypoint /usr/local/bin/alpha_diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alpha_diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beta_diversity.py

```bash
$ singularity exec <container> /usr/local/bin/beta_diversity.py
$ podman run --it --rm --entrypoint /usr/local/bin/beta_diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beta_diversity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_kreports.py

```bash
$ singularity exec <container> /usr/local/bin/combine_kreports.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_kreports.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_kreports.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine_mpa.py

```bash
$ singularity exec <container> /usr/local/bin/combine_mpa.py
$ podman run --it --rm --entrypoint /usr/local/bin/combine_mpa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine_mpa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_kraken_reads.py

```bash
$ singularity exec <container> /usr/local/bin/extract_kraken_reads.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_kraken_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_kraken_reads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_bracken.out.py

```bash
$ singularity exec <container> /usr/local/bin/filter_bracken.out.py
$ podman run --it --rm --entrypoint /usr/local/bin/filter_bracken.out.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_bracken.out.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_unmapped.py

```bash
$ singularity exec <container> /usr/local/bin/fix_unmapped.py
$ podman run --it --rm --entrypoint /usr/local/bin/fix_unmapped.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_unmapped.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kreport2krona.py

```bash
$ singularity exec <container> /usr/local/bin/kreport2krona.py
$ podman run --it --rm --entrypoint /usr/local/bin/kreport2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kreport2krona.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kreport2mpa.py

```bash
$ singularity exec <container> /usr/local/bin/kreport2mpa.py
$ podman run --it --rm --entrypoint /usr/local/bin/kreport2mpa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kreport2mpa.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_kreport.py

```bash
$ singularity exec <container> /usr/local/bin/make_kreport.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_kreport.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_kreport.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_ktaxonomy.py

```bash
$ singularity exec <container> /usr/local/bin/make_ktaxonomy.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_ktaxonomy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_ktaxonomy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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