---
layout: container
name:  "quay.io/biocontainers/keggcharter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/keggcharter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/keggcharter/container.yaml"
updated_at: "2025-10-14 03:12:45.902563"
latest: "1.1.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/keggcharter"
aliases:
 - "KEGGCharter_prokaryotic_maps.txt"
 - "keggcharter.py"
 - "keggpathway_map.py"
 - "pdfsig"
 - "pdfattach"
 - "pdfdetach"
 - "pdffonts"
 - "pdfimages"
 - "pdfinfo"
 - "pdfseparate"
 - "pdftocairo"
 - "pdftohtml"
 - "pdftoppm"
versions:
 - "0.4.0--hdfd78af_0"
 - "0.4.1--hdfd78af_0"
 - "0.4.2--hdfd78af_0"
 - "0.5.0--hdfd78af_0"
 - "0.6.0--hdfd78af_0"
 - "0.5.1--hdfd78af_0"
 - "0.7.0--hdfd78af_0"
 - "0.7.1--hdfd78af_0"
 - "1.0.0--hdfd78af_0"
 - "1.1.2--hdfd78af_0"
 - "1.0.2--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for keggcharter"
config: {"url": "https://biocontainers.pro/tools/keggcharter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for keggcharter", "latest": {"1.1.2--hdfd78af_0": "sha256:89e8cbbb13aa4392f8ca83fa3f4e9bbae40672ef2d7cfcac7c7780c1a2f5a2b0"}, "tags": {"0.4.0--hdfd78af_0": "sha256:5df9959b05dfafa90df13d270b008d606c42e23cfc3bda8c05ffffa407796233", "0.4.1--hdfd78af_0": "sha256:c87e110b83c375d95bc5dcb84c7e71bce82ea53e97a6e451039866b9b7857745", "0.4.2--hdfd78af_0": "sha256:e4e416fe7a4b1d0e4b1008a96cdb6b6538ddf59ecf303daa5e7d1c9fc2471aed", "0.5.0--hdfd78af_0": "sha256:e071c7063e29285c99bfa6df903c9542c08c6548f254b441063a0d35a966ade1", "0.6.0--hdfd78af_0": "sha256:7cd1af809d637522106b4a9ff3de2447be827aeaa3c429b17e16aaeae9a5e697", "0.5.1--hdfd78af_0": "sha256:f9813f1b5c445087a382f0f05960978cebbd6d6f336c0c668611042aea16dc5f", "0.7.0--hdfd78af_0": "sha256:08290f17e44aa884ec96a9b98bb4d710de1e16333f649b447d87890caaa1411e", "0.7.1--hdfd78af_0": "sha256:7b1da26986ed8d3a253f12bb7c61a3bc04ff180caf64d770a92dae83546623b4", "1.0.0--hdfd78af_0": "sha256:ddde5628e972995f9c9aefa4a474331c22f28089ab3378cf87c518658815ea97", "1.1.2--hdfd78af_0": "sha256:89e8cbbb13aa4392f8ca83fa3f4e9bbae40672ef2d7cfcac7c7780c1a2f5a2b0", "1.0.2--hdfd78af_0": "sha256:4facce2b683653e3194fa92c0cc481dcd008dd835116249ec68041b207d6474e"}, "docker": "quay.io/biocontainers/keggcharter", "aliases": {"KEGGCharter_prokaryotic_maps.txt": "/usr/local/bin/KEGGCharter_prokaryotic_maps.txt", "keggcharter.py": "/usr/local/bin/keggcharter.py", "keggpathway_map.py": "/usr/local/bin/keggpathway_map.py", "pdfsig": "/usr/local/bin/pdfsig", "pdfattach": "/usr/local/bin/pdfattach", "pdfdetach": "/usr/local/bin/pdfdetach", "pdffonts": "/usr/local/bin/pdffonts", "pdfimages": "/usr/local/bin/pdfimages", "pdfinfo": "/usr/local/bin/pdfinfo", "pdfseparate": "/usr/local/bin/pdfseparate", "pdftocairo": "/usr/local/bin/pdftocairo", "pdftohtml": "/usr/local/bin/pdftohtml", "pdftoppm": "/usr/local/bin/pdftoppm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/keggcharter.
shpc-registry automated BioContainers addition for keggcharter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/keggcharter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/keggcharter:1.1.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/keggcharter/1.1.2--hdfd78af_0
$ module help quay.io/biocontainers/keggcharter/1.1.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### keggcharter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### keggcharter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### keggcharter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### keggcharter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### keggcharter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### keggcharter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### KEGGCharter_prokaryotic_maps.txt

```bash
$ singularity exec <container> /usr/local/bin/KEGGCharter_prokaryotic_maps.txt
$ podman run --it --rm --entrypoint /usr/local/bin/KEGGCharter_prokaryotic_maps.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KEGGCharter_prokaryotic_maps.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keggcharter.py

```bash
$ singularity exec <container> /usr/local/bin/keggcharter.py
$ podman run --it --rm --entrypoint /usr/local/bin/keggcharter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keggcharter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keggpathway_map.py

```bash
$ singularity exec <container> /usr/local/bin/keggpathway_map.py
$ podman run --it --rm --entrypoint /usr/local/bin/keggpathway_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keggpathway_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfsig

```bash
$ singularity exec <container> /usr/local/bin/pdfsig
$ podman run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfattach

```bash
$ singularity exec <container> /usr/local/bin/pdfattach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfdetach

```bash
$ singularity exec <container> /usr/local/bin/pdfdetach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfdetach   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdffonts

```bash
$ singularity exec <container> /usr/local/bin/pdffonts
$ podman run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdffonts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfimages

```bash
$ singularity exec <container> /usr/local/bin/pdfimages
$ podman run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfimages   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfinfo

```bash
$ singularity exec <container> /usr/local/bin/pdfinfo
$ podman run --it --rm --entrypoint /usr/local/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfseparate

```bash
$ singularity exec <container> /usr/local/bin/pdfseparate
$ podman run --it --rm --entrypoint /usr/local/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfseparate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftocairo

```bash
$ singularity exec <container> /usr/local/bin/pdftocairo
$ podman run --it --rm --entrypoint /usr/local/bin/pdftocairo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftocairo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftohtml

```bash
$ singularity exec <container> /usr/local/bin/pdftohtml
$ podman run --it --rm --entrypoint /usr/local/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftohtml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdftoppm

```bash
$ singularity exec <container> /usr/local/bin/pdftoppm
$ podman run --it --rm --entrypoint /usr/local/bin/pdftoppm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdftoppm   -v ${PWD} -w ${PWD} <container> -c " $@"
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