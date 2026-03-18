---
layout: container
name:  "quay.io/biocontainers/esme_pio_psmpi_4_3_2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_pio_psmpi_4_3_2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_pio_psmpi_4_3_2/container.yaml"
updated_at: "2026-03-18 05:05:27.832273"
latest: "2.6.6--hb2a3317_0"
container_url: "https://biocontainers.pro/tools/esme_pio_psmpi_4_3_2"
aliases:
 - "cxi_atomic_bw"
 - "cxi_atomic_lat"
 - "cxi_device_list"
 - "cxi_dump_csrs"
 - "cxi_gpu_loopback_bw"
 - "cxi_heatsink_check"
 - "cxi_read_bw"
 - "cxi_read_lat"
 - "cxi_rh"
 - "cxi_send_bw"
 - "cxi_send_lat"
 - "cxi_service"
 - "cxi_stat"
 - "cxi_udp_gen"
 - "cxi_write_bw"
 - "cxi_write_lat"
 - "fi_mon_sampler"
 - "mount.fuse3"
 - "pcc"
 - "test_map_csr"
 - "test_write_csr"
 - "fi_info"
 - "fi_pingpong"
 - "fi_strerror"
 - "prte"
 - "prte_info"
 - "prted"
 - "prterun"
 - "pterm"
 - "prun"
 - "nc4print"
 - "ocprint"
 - "chacl"
 - "getfacl"
 - "setfacl"
 - "cdfdiff"
 - "ncmpidiff"
 - "ncmpidump"
 - "ncmpigen"
 - "ncoffsets"
 - "ncvalidator"
 - "pnetcdf-config"
 - "pnetcdf_version"
 - "h5pcc"
 - "h5perf"
 - "h5pfc"
versions:
 - "2.6.6--hb2a3317_0"
description: "singularity registry hpc automated addition for esme_pio_psmpi_4_3_2"
config: {"url": "https://biocontainers.pro/tools/esme_pio_psmpi_4_3_2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_pio_psmpi_4_3_2", "latest": {"2.6.6--hb2a3317_0": "sha256:27cd4c1dc31465f475f723b08bcb8a0201d5742b166e928dabb87c286bbb8179"}, "tags": {"2.6.6--hb2a3317_0": "sha256:27cd4c1dc31465f475f723b08bcb8a0201d5742b166e928dabb87c286bbb8179"}, "docker": "quay.io/biocontainers/esme_pio_psmpi_4_3_2", "aliases": {"cxi_atomic_bw": "/usr/local/bin/cxi_atomic_bw", "cxi_atomic_lat": "/usr/local/bin/cxi_atomic_lat", "cxi_device_list": "/usr/local/bin/cxi_device_list", "cxi_dump_csrs": "/usr/local/bin/cxi_dump_csrs", "cxi_gpu_loopback_bw": "/usr/local/bin/cxi_gpu_loopback_bw", "cxi_heatsink_check": "/usr/local/bin/cxi_heatsink_check", "cxi_read_bw": "/usr/local/bin/cxi_read_bw", "cxi_read_lat": "/usr/local/bin/cxi_read_lat", "cxi_rh": "/usr/local/bin/cxi_rh", "cxi_send_bw": "/usr/local/bin/cxi_send_bw", "cxi_send_lat": "/usr/local/bin/cxi_send_lat", "cxi_service": "/usr/local/bin/cxi_service", "cxi_stat": "/usr/local/bin/cxi_stat", "cxi_udp_gen": "/usr/local/bin/cxi_udp_gen", "cxi_write_bw": "/usr/local/bin/cxi_write_bw", "cxi_write_lat": "/usr/local/bin/cxi_write_lat", "fi_mon_sampler": "/usr/local/bin/fi_mon_sampler", "mount.fuse3": "/usr/local/bin/mount.fuse3", "pcc": "/usr/local/bin/pcc", "test_map_csr": "/usr/local/bin/test_map_csr", "test_write_csr": "/usr/local/bin/test_write_csr", "fi_info": "/usr/local/bin/fi_info", "fi_pingpong": "/usr/local/bin/fi_pingpong", "fi_strerror": "/usr/local/bin/fi_strerror", "prte": "/usr/local/bin/prte", "prte_info": "/usr/local/bin/prte_info", "prted": "/usr/local/bin/prted", "prterun": "/usr/local/bin/prterun", "pterm": "/usr/local/bin/pterm", "prun": "/usr/local/bin/prun", "nc4print": "/usr/local/bin/nc4print", "ocprint": "/usr/local/bin/ocprint", "chacl": "/usr/local/bin/chacl", "getfacl": "/usr/local/bin/getfacl", "setfacl": "/usr/local/bin/setfacl", "cdfdiff": "/usr/local/bin/cdfdiff", "ncmpidiff": "/usr/local/bin/ncmpidiff", "ncmpidump": "/usr/local/bin/ncmpidump", "ncmpigen": "/usr/local/bin/ncmpigen", "ncoffsets": "/usr/local/bin/ncoffsets", "ncvalidator": "/usr/local/bin/ncvalidator", "pnetcdf-config": "/usr/local/bin/pnetcdf-config", "pnetcdf_version": "/usr/local/bin/pnetcdf_version", "h5pcc": "/usr/local/bin/h5pcc", "h5perf": "/usr/local/bin/h5perf", "h5pfc": "/usr/local/bin/h5pfc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_pio_psmpi_4_3_2.
singularity registry hpc automated addition for esme_pio_psmpi_4_3_2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_pio_psmpi_4_3_2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_pio_psmpi_4_3_2:2.6.6--hb2a3317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_pio_psmpi_4_3_2/2.6.6--hb2a3317_0
$ module help quay.io/biocontainers/esme_pio_psmpi_4_3_2/2.6.6--hb2a3317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_pio_psmpi_4_3_2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_pio_psmpi_4_3_2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_pio_psmpi_4_3_2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_pio_psmpi_4_3_2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_pio_psmpi_4_3_2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_pio_psmpi_4_3_2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cxi_atomic_bw

```bash
$ singularity exec <container> /usr/local/bin/cxi_atomic_bw
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_atomic_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_atomic_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_atomic_lat

```bash
$ singularity exec <container> /usr/local/bin/cxi_atomic_lat
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_atomic_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_atomic_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_device_list

```bash
$ singularity exec <container> /usr/local/bin/cxi_device_list
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_device_list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_device_list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_dump_csrs

```bash
$ singularity exec <container> /usr/local/bin/cxi_dump_csrs
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_dump_csrs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_dump_csrs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_gpu_loopback_bw

```bash
$ singularity exec <container> /usr/local/bin/cxi_gpu_loopback_bw
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_gpu_loopback_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_gpu_loopback_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_heatsink_check

```bash
$ singularity exec <container> /usr/local/bin/cxi_heatsink_check
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_heatsink_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_heatsink_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_read_bw

```bash
$ singularity exec <container> /usr/local/bin/cxi_read_bw
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_read_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_read_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_read_lat

```bash
$ singularity exec <container> /usr/local/bin/cxi_read_lat
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_read_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_read_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_rh

```bash
$ singularity exec <container> /usr/local/bin/cxi_rh
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_rh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_rh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_send_bw

```bash
$ singularity exec <container> /usr/local/bin/cxi_send_bw
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_send_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_send_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_send_lat

```bash
$ singularity exec <container> /usr/local/bin/cxi_send_lat
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_send_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_send_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_service

```bash
$ singularity exec <container> /usr/local/bin/cxi_service
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_service   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_service   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_stat

```bash
$ singularity exec <container> /usr/local/bin/cxi_stat
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_stat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_stat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_udp_gen

```bash
$ singularity exec <container> /usr/local/bin/cxi_udp_gen
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_udp_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_udp_gen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_write_bw

```bash
$ singularity exec <container> /usr/local/bin/cxi_write_bw
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_write_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_write_bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cxi_write_lat

```bash
$ singularity exec <container> /usr/local/bin/cxi_write_lat
$ podman run --it --rm --entrypoint /usr/local/bin/cxi_write_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cxi_write_lat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fi_mon_sampler

```bash
$ singularity exec <container> /usr/local/bin/fi_mon_sampler
$ podman run --it --rm --entrypoint /usr/local/bin/fi_mon_sampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fi_mon_sampler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mount.fuse3

```bash
$ singularity exec <container> /usr/local/bin/mount.fuse3
$ podman run --it --rm --entrypoint /usr/local/bin/mount.fuse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mount.fuse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcc

```bash
$ singularity exec <container> /usr/local/bin/pcc
$ podman run --it --rm --entrypoint /usr/local/bin/pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_map_csr

```bash
$ singularity exec <container> /usr/local/bin/test_map_csr
$ podman run --it --rm --entrypoint /usr/local/bin/test_map_csr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_map_csr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_write_csr

```bash
$ singularity exec <container> /usr/local/bin/test_write_csr
$ podman run --it --rm --entrypoint /usr/local/bin/test_write_csr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_write_csr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fi_info

```bash
$ singularity exec <container> /usr/local/bin/fi_info
$ podman run --it --rm --entrypoint /usr/local/bin/fi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fi_pingpong

```bash
$ singularity exec <container> /usr/local/bin/fi_pingpong
$ podman run --it --rm --entrypoint /usr/local/bin/fi_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fi_pingpong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fi_strerror

```bash
$ singularity exec <container> /usr/local/bin/fi_strerror
$ podman run --it --rm --entrypoint /usr/local/bin/fi_strerror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fi_strerror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prte

```bash
$ singularity exec <container> /usr/local/bin/prte
$ podman run --it --rm --entrypoint /usr/local/bin/prte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prte_info

```bash
$ singularity exec <container> /usr/local/bin/prte_info
$ podman run --it --rm --entrypoint /usr/local/bin/prte_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prted

```bash
$ singularity exec <container> /usr/local/bin/prted
$ podman run --it --rm --entrypoint /usr/local/bin/prted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prterun

```bash
$ singularity exec <container> /usr/local/bin/prterun
$ podman run --it --rm --entrypoint /usr/local/bin/prterun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prterun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pterm

```bash
$ singularity exec <container> /usr/local/bin/pterm
$ podman run --it --rm --entrypoint /usr/local/bin/pterm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pterm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prun

```bash
$ singularity exec <container> /usr/local/bin/prun
$ podman run --it --rm --entrypoint /usr/local/bin/prun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc4print

```bash
$ singularity exec <container> /usr/local/bin/nc4print
$ podman run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocprint

```bash
$ singularity exec <container> /usr/local/bin/ocprint
$ podman run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chacl

```bash
$ singularity exec <container> /usr/local/bin/chacl
$ podman run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfacl

```bash
$ singularity exec <container> /usr/local/bin/getfacl
$ podman run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setfacl

```bash
$ singularity exec <container> /usr/local/bin/setfacl
$ podman run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdfdiff

```bash
$ singularity exec <container> /usr/local/bin/cdfdiff
$ podman run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidiff

```bash
$ singularity exec <container> /usr/local/bin/ncmpidiff
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidump

```bash
$ singularity exec <container> /usr/local/bin/ncmpidump
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpigen

```bash
$ singularity exec <container> /usr/local/bin/ncmpigen
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncoffsets

```bash
$ singularity exec <container> /usr/local/bin/ncoffsets
$ podman run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncvalidator

```bash
$ singularity exec <container> /usr/local/bin/ncvalidator
$ podman run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf-config

```bash
$ singularity exec <container> /usr/local/bin/pnetcdf-config
$ podman run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf_version

```bash
$ singularity exec <container> /usr/local/bin/pnetcdf_version
$ podman run --it --rm --entrypoint /usr/local/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pcc

```bash
$ singularity exec <container> /usr/local/bin/h5pcc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf

```bash
$ singularity exec <container> /usr/local/bin/h5perf
$ podman run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pfc

```bash
$ singularity exec <container> /usr/local/bin/h5pfc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
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