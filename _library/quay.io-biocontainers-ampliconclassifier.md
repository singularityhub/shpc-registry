---
layout: container
name:  "quay.io/biocontainers/ampliconclassifier"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ampliconclassifier/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ampliconclassifier/container.yaml"
updated_at: "2023-12-16 03:07:34.266278"
latest: "0.4.14--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ampliconclassifier"
aliases:
 - "amplicon_classifier.py"
 - "amplicon_similarity.py"
 - "amplicons_intersecting_bed.py"
 - "feature_similarity.py"
 - "make_input.sh"
 - "make_results_table.py"
 - "softlink_images.py"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.10"
 - "img2webp"
 - "cwebp"
 - "dwebp"
 - "gif2webp"
versions:
 - "0.4.9--hdfd78af_0"
 - "0.4.14--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for ampliconclassifier"
config: {"url": "https://biocontainers.pro/tools/ampliconclassifier", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ampliconclassifier", "latest": {"0.4.14--hdfd78af_0": "sha256:ac2c6ea300c53e5905d0709e0df3e6c862bfa910f7a524d3be0db24b28742127"}, "tags": {"0.4.9--hdfd78af_0": "sha256:8ddbfa465577dda20b88265f5971469d37436039f91688ebb703f0c89263e5c5", "0.4.14--hdfd78af_0": "sha256:ac2c6ea300c53e5905d0709e0df3e6c862bfa910f7a524d3be0db24b28742127"}, "docker": "quay.io/biocontainers/ampliconclassifier", "aliases": {"amplicon_classifier.py": "/usr/local/bin/amplicon_classifier.py", "amplicon_similarity.py": "/usr/local/bin/amplicon_similarity.py", "amplicons_intersecting_bed.py": "/usr/local/bin/amplicons_intersecting_bed.py", "feature_similarity.py": "/usr/local/bin/feature_similarity.py", "make_input.sh": "/usr/local/bin/make_input.sh", "make_results_table.py": "/usr/local/bin/make_results_table.py", "softlink_images.py": "/usr/local/bin/softlink_images.py", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "img2webp": "/usr/local/bin/img2webp", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "gif2webp": "/usr/local/bin/gif2webp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ampliconclassifier.
shpc-registry automated BioContainers addition for ampliconclassifier
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ampliconclassifier
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ampliconclassifier:0.4.14--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ampliconclassifier/0.4.14--hdfd78af_0
$ module help quay.io/biocontainers/ampliconclassifier/0.4.14--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ampliconclassifier-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ampliconclassifier-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ampliconclassifier-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ampliconclassifier-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ampliconclassifier-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ampliconclassifier-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amplicon_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/amplicon_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/amplicon_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicon_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amplicon_similarity.py

```bash
$ singularity exec <container> /usr/local/bin/amplicon_similarity.py
$ podman run --it --rm --entrypoint /usr/local/bin/amplicon_similarity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicon_similarity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amplicons_intersecting_bed.py

```bash
$ singularity exec <container> /usr/local/bin/amplicons_intersecting_bed.py
$ podman run --it --rm --entrypoint /usr/local/bin/amplicons_intersecting_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicons_intersecting_bed.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### feature_similarity.py

```bash
$ singularity exec <container> /usr/local/bin/feature_similarity.py
$ podman run --it --rm --entrypoint /usr/local/bin/feature_similarity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/feature_similarity.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_input.sh

```bash
$ singularity exec <container> /usr/local/bin/make_input.sh
$ podman run --it --rm --entrypoint /usr/local/bin/make_input.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_input.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_results_table.py

```bash
$ singularity exec <container> /usr/local/bin/make_results_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/make_results_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_results_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### softlink_images.py

```bash
$ singularity exec <container> /usr/local/bin/softlink_images.py
$ podman run --it --rm --entrypoint /usr/local/bin/softlink_images.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/softlink_images.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### img2webp

```bash
$ singularity exec <container> /usr/local/bin/img2webp
$ podman run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2webp

```bash
$ singularity exec <container> /usr/local/bin/gif2webp
$ podman run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
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