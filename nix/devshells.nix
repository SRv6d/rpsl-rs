{ pkgs, rustToolchain }:

{
  default = pkgs.mkShell {
    packages = with pkgs; [
      rustToolchain
      rust-analyzer
      cargo-deny
      git
      just
      gh
    ];
  };
}
