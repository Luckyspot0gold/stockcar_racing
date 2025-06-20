// Add to ALL payable functions
uint256 private _status;
modifier nonReentrant() {
    require(_status != 2, "ReentrancyGuard: reentrant call");
    _status = 2;
    _;
    _status = 1;
}
