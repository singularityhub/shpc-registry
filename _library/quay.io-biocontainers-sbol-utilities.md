---
layout: container
name:  "quay.io/biocontainers/sbol-utilities"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sbol-utilities/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sbol-utilities/container.yaml"
updated_at: "2024-03-19 02:41:42.248021"
latest: "1.0a17--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sbol-utilities"
aliases:
 - "corepack"
 - "excel-to-sbol"
 - "fasta2sbol"
 - "genbank2sbol"
 - "graph-sbol"
 - "node"
 - "npm"
 - "npx"
 - "owlrl"
 - "pyshacl"
 - "sbol-calculate-sequences"
 - "sbol-converter"
 - "sbol-diff"
 - "sbol-expand-derivations"
 - "sbol2fasta"
 - "sbol2genbank"
 - "sbol2to3"
 - "sbol3to2"
 - "xml2-config.bak"
 - "csv2rdf"
 - "rdf2dot"
 - "rdfgraphisomorphism"
 - "rdfpipe"
 - "rdfs2dot"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "diffimg"
 - "delaunay"
 - "gts-config"
 - "gts2dxf"
 - "gts2oogl"
 - "gts2stl"
 - "gtscheck"
 - "gtscompare"
 - "gtstemplate"
 - "stl2gts"
 - "transform"
 - "rsvg-convert"
 - "gtk-builder-convert"
 - "gtk-demo"
 - "gtk-query-immodules-2.0"
 - "gtk-update-icon-cache"
versions:
 - "1.0a16--pyhdfd78af_0"
 - "1.0a17--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sbol-utilities"
config: {"url": "https://biocontainers.pro/tools/sbol-utilities", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sbol-utilities", "latest": {"1.0a17--pyhdfd78af_0": "sha256:f0c6dd2ed3ee860d3796b42212c036e9fe5c77148e92289787b37026967be8bc"}, "tags": {"1.0a16--pyhdfd78af_0": "sha256:0d48dd44a56e227f67ce1ae3a243bc001cddc68feeed413dc0298a4addfc7d0f", "1.0a17--pyhdfd78af_0": "sha256:f0c6dd2ed3ee860d3796b42212c036e9fe5c77148e92289787b37026967be8bc"}, "docker": "quay.io/biocontainers/sbol-utilities", "aliases": {"corepack": "/usr/local/bin/corepack", "excel-to-sbol": "/usr/local/bin/excel-to-sbol", "fasta2sbol": "/usr/local/bin/fasta2sbol", "genbank2sbol": "/usr/local/bin/genbank2sbol", "graph-sbol": "/usr/local/bin/graph-sbol", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "npx": "/usr/local/bin/npx", "owlrl": "/usr/local/bin/owlrl", "pyshacl": "/usr/local/bin/pyshacl", "sbol-calculate-sequences": "/usr/local/bin/sbol-calculate-sequences", "sbol-converter": "/usr/local/bin/sbol-converter", "sbol-diff": "/usr/local/bin/sbol-diff", "sbol-expand-derivations": "/usr/local/bin/sbol-expand-derivations", "sbol2fasta": "/usr/local/bin/sbol2fasta", "sbol2genbank": "/usr/local/bin/sbol2genbank", "sbol2to3": "/usr/local/bin/sbol2to3", "sbol3to2": "/usr/local/bin/sbol3to2", "xml2-config.bak": "/usr/local/bin/xml2-config.bak", "csv2rdf": "/usr/local/bin/csv2rdf", "rdf2dot": "/usr/local/bin/rdf2dot", "rdfgraphisomorphism": "/usr/local/bin/rdfgraphisomorphism", "rdfpipe": "/usr/local/bin/rdfpipe", "rdfs2dot": "/usr/local/bin/rdfs2dot", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "diffimg": "/usr/local/bin/diffimg", "delaunay": "/usr/local/bin/delaunay", "gts-config": "/usr/local/bin/gts-config", "gts2dxf": "/usr/local/bin/gts2dxf", "gts2oogl": "/usr/local/bin/gts2oogl", "gts2stl": "/usr/local/bin/gts2stl", "gtscheck": "/usr/local/bin/gtscheck", "gtscompare": "/usr/local/bin/gtscompare", "gtstemplate": "/usr/local/bin/gtstemplate", "stl2gts": "/usr/local/bin/stl2gts", "transform": "/usr/local/bin/transform", "rsvg-convert": "/usr/local/bin/rsvg-convert", "gtk-builder-convert": "/usr/local/bin/gtk-builder-convert", "gtk-demo": "/usr/local/bin/gtk-demo", "gtk-query-immodules-2.0": "/usr/local/bin/gtk-query-immodules-2.0", "gtk-update-icon-cache": "/usr/local/bin/gtk-update-icon-cache"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sbol-utilities.
singularity registry hpc automated addition for sbol-utilities
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sbol-utilities
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sbol-utilities:1.0a17--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sbol-utilities/1.0a17--pyhdfd78af_0
$ module help quay.io/biocontainers/sbol-utilities/1.0a17--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sbol-utilities-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sbol-utilities-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sbol-utilities-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sbol-utilities-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sbol-utilities-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sbol-utilities-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### excel-to-sbol

```bash
$ singularity exec <container> /usr/local/bin/excel-to-sbol
$ podman run --it --rm --entrypoint /usr/local/bin/excel-to-sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/excel-to-sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2sbol

```bash
$ singularity exec <container> /usr/local/bin/fasta2sbol
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genbank2sbol

```bash
$ singularity exec <container> /usr/local/bin/genbank2sbol
$ podman run --it --rm --entrypoint /usr/local/bin/genbank2sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genbank2sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph-sbol

```bash
$ singularity exec <container> /usr/local/bin/graph-sbol
$ podman run --it --rm --entrypoint /usr/local/bin/graph-sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph-sbol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### owlrl

```bash
$ singularity exec <container> /usr/local/bin/owlrl
$ podman run --it --rm --entrypoint /usr/local/bin/owlrl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/owlrl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyshacl

```bash
$ singularity exec <container> /usr/local/bin/pyshacl
$ podman run --it --rm --entrypoint /usr/local/bin/pyshacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyshacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol-calculate-sequences

```bash
$ singularity exec <container> /usr/local/bin/sbol-calculate-sequences
$ podman run --it --rm --entrypoint /usr/local/bin/sbol-calculate-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol-calculate-sequences   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol-converter

```bash
$ singularity exec <container> /usr/local/bin/sbol-converter
$ podman run --it --rm --entrypoint /usr/local/bin/sbol-converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol-converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol-diff

```bash
$ singularity exec <container> /usr/local/bin/sbol-diff
$ podman run --it --rm --entrypoint /usr/local/bin/sbol-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol-expand-derivations

```bash
$ singularity exec <container> /usr/local/bin/sbol-expand-derivations
$ podman run --it --rm --entrypoint /usr/local/bin/sbol-expand-derivations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol-expand-derivations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol2fasta

```bash
$ singularity exec <container> /usr/local/bin/sbol2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/sbol2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol2genbank

```bash
$ singularity exec <container> /usr/local/bin/sbol2genbank
$ podman run --it --rm --entrypoint /usr/local/bin/sbol2genbank   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol2genbank   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol2to3

```bash
$ singularity exec <container> /usr/local/bin/sbol2to3
$ podman run --it --rm --entrypoint /usr/local/bin/sbol2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sbol3to2

```bash
$ singularity exec <container> /usr/local/bin/sbol3to2
$ podman run --it --rm --entrypoint /usr/local/bin/sbol3to2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sbol3to2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdf2dot

```bash
$ singularity exec <container> /usr/local/bin/rdf2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdf2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfgraphisomorphism

```bash
$ singularity exec <container> /usr/local/bin/rdfgraphisomorphism
$ podman run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfgraphisomorphism   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfpipe

```bash
$ singularity exec <container> /usr/local/bin/rdfpipe
$ podman run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfpipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdfs2dot

```bash
$ singularity exec <container> /usr/local/bin/rdfs2dot
$ podman run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdfs2dot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### diffimg

```bash
$ singularity exec <container> /usr/local/bin/diffimg
$ podman run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diffimg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### delaunay

```bash
$ singularity exec <container> /usr/local/bin/delaunay
$ podman run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts-config

```bash
$ singularity exec <container> /usr/local/bin/gts-config
$ podman run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2dxf

```bash
$ singularity exec <container> /usr/local/bin/gts2dxf
$ podman run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2dxf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2oogl

```bash
$ singularity exec <container> /usr/local/bin/gts2oogl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2oogl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gts2stl

```bash
$ singularity exec <container> /usr/local/bin/gts2stl
$ podman run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gts2stl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscheck

```bash
$ singularity exec <container> /usr/local/bin/gtscheck
$ podman run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtscompare

```bash
$ singularity exec <container> /usr/local/bin/gtscompare
$ podman run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtscompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtstemplate

```bash
$ singularity exec <container> /usr/local/bin/gtstemplate
$ podman run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtstemplate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stl2gts

```bash
$ singularity exec <container> /usr/local/bin/stl2gts
$ podman run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stl2gts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transform

```bash
$ singularity exec <container> /usr/local/bin/transform
$ podman run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsvg-convert

```bash
$ singularity exec <container> /usr/local/bin/rsvg-convert
$ podman run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-convert

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-demo

```bash
$ singularity exec <container> /usr/local/bin/gtk-demo
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-2.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-2.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-update-icon-cache

```bash
$ singularity exec <container> /usr/local/bin/gtk-update-icon-cache
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
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