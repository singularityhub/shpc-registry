---
layout: container
name:  "quay.io/biocontainers/scicone"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scicone/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scicone/container.yaml"
updated_at: "2026-10-10 19:34:31.186532"
latest: "1.0.0--py310hbebfe88_0"
container_url: "https://biocontainers.pro/tools/scicone"
aliases:
 - "scicone-breakpoint_detection"
 - "scicone-inference"
 - "scicone-score"
 - "scicone-simulation"
 - "dot_sandbox"
 - "gtk-builder-tool"
 - "gtk-encode-symbolic-svg"
 - "gtk-launch"
 - "gtk-query-immodules-3.0"
 - "gtk-query-settings"
 - "igraph"
 - "wayland-scanner"
 - "idna"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "hb-raster"
 - "hb-vector"
 - "fc-genconf"
 - "h2benchmark"
 - "checksum-profile"
 - "diffimg"
 - "delaunay"
 - "gts-config"
 - "gts2dxf"
 - "gts2oogl"
 - "gts2stl"
 - "gtscheck"
 - "gtscompare"
versions:
 - "1.0.0--py310hbebfe88_0"
description: "singularity registry hpc automated addition for scicone"
config: {"url": "https://biocontainers.pro/tools/scicone", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for scicone", "latest": {"1.0.0--py310hbebfe88_0": "sha256:cace263467c472160c894d80001ef1fe10b631d80bb641a0df3ca39f73a8c800"}, "tags": {"1.0.0--py310hbebfe88_0": "sha256:cace263467c472160c894d80001ef1fe10b631d80bb641a0df3ca39f73a8c800"}, "docker": "quay.io/biocontainers/scicone", "aliases": {"scicone-breakpoint_detection": "/usr/local/bin/scicone-breakpoint_detection", "scicone-inference": "/usr/local/bin/scicone-inference", "scicone-score": "/usr/local/bin/scicone-score", "scicone-simulation": "/usr/local/bin/scicone-simulation", "dot_sandbox": "/usr/local/bin/dot_sandbox", "gtk-builder-tool": "/usr/local/bin/gtk-builder-tool", "gtk-encode-symbolic-svg": "/usr/local/bin/gtk-encode-symbolic-svg", "gtk-launch": "/usr/local/bin/gtk-launch", "gtk-query-immodules-3.0": "/usr/local/bin/gtk-query-immodules-3.0", "gtk-query-settings": "/usr/local/bin/gtk-query-settings", "igraph": "/usr/local/bin/igraph", "wayland-scanner": "/usr/local/bin/wayland-scanner", "idna": "/usr/local/bin/idna", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "fc-genconf": "/usr/local/bin/fc-genconf", "h2benchmark": "/usr/local/bin/h2benchmark", "checksum-profile": "/usr/local/bin/checksum-profile", "diffimg": "/usr/local/bin/diffimg", "delaunay": "/usr/local/bin/delaunay", "gts-config": "/usr/local/bin/gts-config", "gts2dxf": "/usr/local/bin/gts2dxf", "gts2oogl": "/usr/local/bin/gts2oogl", "gts2stl": "/usr/local/bin/gts2stl", "gtscheck": "/usr/local/bin/gtscheck", "gtscompare": "/usr/local/bin/gtscompare"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scicone.
singularity registry hpc automated addition for scicone
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scicone
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scicone:1.0.0--py310hbebfe88_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scicone/1.0.0--py310hbebfe88_0
$ module help quay.io/biocontainers/scicone/1.0.0--py310hbebfe88_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scicone-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scicone-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scicone-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scicone-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scicone-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scicone-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scicone-breakpoint_detection

```bash
$ singularity exec <container> /usr/local/bin/scicone-breakpoint_detection
$ podman run --it --rm --entrypoint /usr/local/bin/scicone-breakpoint_detection   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scicone-breakpoint_detection   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scicone-inference

```bash
$ singularity exec <container> /usr/local/bin/scicone-inference
$ podman run --it --rm --entrypoint /usr/local/bin/scicone-inference   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scicone-inference   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scicone-score

```bash
$ singularity exec <container> /usr/local/bin/scicone-score
$ podman run --it --rm --entrypoint /usr/local/bin/scicone-score   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scicone-score   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scicone-simulation

```bash
$ singularity exec <container> /usr/local/bin/scicone-simulation
$ podman run --it --rm --entrypoint /usr/local/bin/scicone-simulation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scicone-simulation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dot_sandbox

```bash
$ singularity exec <container> /usr/local/bin/dot_sandbox
$ podman run --it --rm --entrypoint /usr/local/bin/dot_sandbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dot_sandbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-encode-symbolic-svg

```bash
$ singularity exec <container> /usr/local/bin/gtk-encode-symbolic-svg
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-launch

```bash
$ singularity exec <container> /usr/local/bin/gtk-launch
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-3.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-settings

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-settings
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-compile-repository

```bash
$ singularity exec <container> /usr/local/bin/gi-compile-repository
$ podman run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-decompile-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-decompile-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-inspect-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-inspect-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
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