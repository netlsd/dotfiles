import XMonad
import XMonad.Hooks.ManageDocks
import XMonad.Util.EZConfig
import qualified Data.Map as M
import XMonad.Actions.GroupNavigation

myWorkspaces = ["web","terminal","dev","virt","doc","temp","7","8","9"]

myManageHook = composeAll
   [ className =? "firefox"   --> doShift "web"
   --, className =? "urxvt"     --> doShift "terminal"
   , className =? "jetbrains-studio"  --> doShift "dev"
   , manageDocks
   ]

myKeys conf@(XConfig {modMask = modm}) = M.fromList $
   [ ((modm, xK_Return), spawn "urxvt") 
   , ((modm, xK_f), spawn "firefox")
   , ((0, xK_F3), spawn "dmenu_run")
   , ((modm, xK_Escape), nextMatch History (return True)) ]

main = xmonad $ def
   { workspaces = myWorkspaces
   , modMask = mod4Mask
   --, keys = myKeys
   , keys = \c -> myKeys c `M.union` keys def c
   , manageHook = myManageHook <+> manageHook def
   , terminal = "xterm"
   , logHook = historyHook
   }
