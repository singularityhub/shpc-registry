---
layout: container
name:  "quay.io/biocontainers/nomnom"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nomnom/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nomnom/container.yaml"
updated_at: "2026-03-13 16:46:23.272307"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nomnom"
aliases:
 - "cat-numbers"
 - "compact-json"
 - "csv2numbers"
 - "csv2ods"
 - "mailodf"
 - "nomnom"
 - "odf2mht"
 - "odf2xhtml"
 - "odf2xml"
 - "odfimgimport"
 - "odflint"
 - "odfmeta"
 - "odfoutline"
 - "odfuserfield"
 - "unpack-numbers"
 - "xml2odf"
 - "runxlrd.py"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "pygmentize"
 - "numpy-config"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for nomnom"
config: {"url": "https://biocontainers.pro/tools/nomnom", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nomnom", "latest": {"0.1.0--pyhdfd78af_0": "sha256:835e71fefbaff52ded42e1384a2b3d7dd1bcc60325ba20e759d2112ee935cbd6"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:835e71fefbaff52ded42e1384a2b3d7dd1bcc60325ba20e759d2112ee935cbd6"}, "docker": "quay.io/biocontainers/nomnom", "aliases": {"cat-numbers": "/usr/local/bin/cat-numbers", "compact-json": "/usr/local/bin/compact-json", "csv2numbers": "/usr/local/bin/csv2numbers", "csv2ods": "/usr/local/bin/csv2ods", "mailodf": "/usr/local/bin/mailodf", "nomnom": "/usr/local/bin/nomnom", "odf2mht": "/usr/local/bin/odf2mht", "odf2xhtml": "/usr/local/bin/odf2xhtml", "odf2xml": "/usr/local/bin/odf2xml", "odfimgimport": "/usr/local/bin/odfimgimport", "odflint": "/usr/local/bin/odflint", "odfmeta": "/usr/local/bin/odfmeta", "odfoutline": "/usr/local/bin/odfoutline", "odfuserfield": "/usr/local/bin/odfuserfield", "unpack-numbers": "/usr/local/bin/unpack-numbers", "xml2odf": "/usr/local/bin/xml2odf", "runxlrd.py": "/usr/local/bin/runxlrd.py", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "pygmentize": "/usr/local/bin/pygmentize", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nomnom.
singularity registry hpc automated addition for nomnom
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nomnom
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nomnom:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nomnom/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/nomnom/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nomnom-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nomnom-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nomnom-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nomnom-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nomnom-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nomnom-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cat-numbers

```bash
$ singularity exec <container> /usr/local/bin/cat-numbers
$ podman run --it --rm --entrypoint /usr/local/bin/cat-numbers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat-numbers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compact-json

```bash
$ singularity exec <container> /usr/local/bin/compact-json
$ podman run --it --rm --entrypoint /usr/local/bin/compact-json   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compact-json   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2numbers

```bash
$ singularity exec <container> /usr/local/bin/csv2numbers
$ podman run --it --rm --entrypoint /usr/local/bin/csv2numbers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2numbers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2ods

```bash
$ singularity exec <container> /usr/local/bin/csv2ods
$ podman run --it --rm --entrypoint /usr/local/bin/csv2ods   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2ods   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mailodf

```bash
$ singularity exec <container> /usr/local/bin/mailodf
$ podman run --it --rm --entrypoint /usr/local/bin/mailodf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mailodf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nomnom

```bash
$ singularity exec <container> /usr/local/bin/nomnom
$ podman run --it --rm --entrypoint /usr/local/bin/nomnom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nomnom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odf2mht

```bash
$ singularity exec <container> /usr/local/bin/odf2mht
$ podman run --it --rm --entrypoint /usr/local/bin/odf2mht   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odf2mht   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odf2xhtml

```bash
$ singularity exec <container> /usr/local/bin/odf2xhtml
$ podman run --it --rm --entrypoint /usr/local/bin/odf2xhtml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odf2xhtml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odf2xml

```bash
$ singularity exec <container> /usr/local/bin/odf2xml
$ podman run --it --rm --entrypoint /usr/local/bin/odf2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odf2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odfimgimport

```bash
$ singularity exec <container> /usr/local/bin/odfimgimport
$ podman run --it --rm --entrypoint /usr/local/bin/odfimgimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odfimgimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odflint

```bash
$ singularity exec <container> /usr/local/bin/odflint
$ podman run --it --rm --entrypoint /usr/local/bin/odflint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odflint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odfmeta

```bash
$ singularity exec <container> /usr/local/bin/odfmeta
$ podman run --it --rm --entrypoint /usr/local/bin/odfmeta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odfmeta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odfoutline

```bash
$ singularity exec <container> /usr/local/bin/odfoutline
$ podman run --it --rm --entrypoint /usr/local/bin/odfoutline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odfoutline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### odfuserfield

```bash
$ singularity exec <container> /usr/local/bin/odfuserfield
$ podman run --it --rm --entrypoint /usr/local/bin/odfuserfield   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/odfuserfield   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpack-numbers

```bash
$ singularity exec <container> /usr/local/bin/unpack-numbers
$ podman run --it --rm --entrypoint /usr/local/bin/unpack-numbers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpack-numbers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml2odf

```bash
$ singularity exec <container> /usr/local/bin/xml2odf
$ podman run --it --rm --entrypoint /usr/local/bin/xml2odf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2odf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runxlrd.py

```bash
$ singularity exec <container> /usr/local/bin/runxlrd.py
$ podman run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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