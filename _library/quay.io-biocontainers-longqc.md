---
layout: container
name:  "quay.io/biocontainers/longqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longqc/container.yaml"
updated_at: "2023-08-21 03:04:40.695173"
latest: "1.2.0c--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/longqc"
aliases:
 - "_version.py"
 - "longQC.py"
 - "lq_adapt.py"
 - "lq_coverage.py"
 - "lq_exec.py"
 - "lq_gamma.py"
 - "lq_gcfrac.py"
 - "lq_mask.py"
 - "lq_nanopore.py"
 - "lq_rs.py"
 - "lq_sequel.py"
 - "lq_utils.py"
 - "minimap2-coverage"
 - "mirror_server"
 - "mirror_server_stop"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
versions:
 - "1.2.0c--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for longqc"
config: {"url": "https://biocontainers.pro/tools/longqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for longqc", "latest": {"1.2.0c--hdfd78af_0": "sha256:da5016444c31af60d75262f182fa0d398b78f9579468c15c2104c9475af2dc9a"}, "tags": {"1.2.0c--hdfd78af_0": "sha256:da5016444c31af60d75262f182fa0d398b78f9579468c15c2104c9475af2dc9a"}, "docker": "quay.io/biocontainers/longqc", "aliases": {"_version.py": "/usr/local/bin/_version.py", "longQC.py": "/usr/local/bin/longQC.py", "lq_adapt.py": "/usr/local/bin/lq_adapt.py", "lq_coverage.py": "/usr/local/bin/lq_coverage.py", "lq_exec.py": "/usr/local/bin/lq_exec.py", "lq_gamma.py": "/usr/local/bin/lq_gamma.py", "lq_gcfrac.py": "/usr/local/bin/lq_gcfrac.py", "lq_mask.py": "/usr/local/bin/lq_mask.py", "lq_nanopore.py": "/usr/local/bin/lq_nanopore.py", "lq_rs.py": "/usr/local/bin/lq_rs.py", "lq_sequel.py": "/usr/local/bin/lq_sequel.py", "lq_utils.py": "/usr/local/bin/lq_utils.py", "minimap2-coverage": "/usr/local/bin/minimap2-coverage", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longqc.
shpc-registry automated BioContainers addition for longqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longqc:1.2.0c--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longqc/1.2.0c--hdfd78af_0
$ module help quay.io/biocontainers/longqc/1.2.0c--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _version.py

```bash
$ singularity exec <container> /usr/local/bin/_version.py
$ podman run --it --rm --entrypoint /usr/local/bin/_version.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_version.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### longQC.py

```bash
$ singularity exec <container> /usr/local/bin/longQC.py
$ podman run --it --rm --entrypoint /usr/local/bin/longQC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longQC.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_adapt.py

```bash
$ singularity exec <container> /usr/local/bin/lq_adapt.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_adapt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_adapt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_coverage.py

```bash
$ singularity exec <container> /usr/local/bin/lq_coverage.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_coverage.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_exec.py

```bash
$ singularity exec <container> /usr/local/bin/lq_exec.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_exec.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_exec.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_gamma.py

```bash
$ singularity exec <container> /usr/local/bin/lq_gamma.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_gamma.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_gamma.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_gcfrac.py

```bash
$ singularity exec <container> /usr/local/bin/lq_gcfrac.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_gcfrac.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_gcfrac.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_mask.py

```bash
$ singularity exec <container> /usr/local/bin/lq_mask.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_mask.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_mask.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_nanopore.py

```bash
$ singularity exec <container> /usr/local/bin/lq_nanopore.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_nanopore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_nanopore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_rs.py

```bash
$ singularity exec <container> /usr/local/bin/lq_rs.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_rs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_rs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_sequel.py

```bash
$ singularity exec <container> /usr/local/bin/lq_sequel.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_sequel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_sequel.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lq_utils.py

```bash
$ singularity exec <container> /usr/local/bin/lq_utils.py
$ podman run --it --rm --entrypoint /usr/local/bin/lq_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lq_utils.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2-coverage

```bash
$ singularity exec <container> /usr/local/bin/minimap2-coverage
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2-coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
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