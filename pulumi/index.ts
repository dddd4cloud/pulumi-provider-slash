import * as slash from "@cloudyskysoftware/pulumi-slash";

import * as o from "@cloudyskysoftware/pulumi-slash/types/output";

const service = new slash.api.ShortcutServiceShortcut("my-shortcut", {
    name: "My service",
    link: "https://github.com/praneetloke/test",

});

export const shortcutId = service.shortcut.apply(
    (d) => (d as o.api.Apiv1Shortcut).id

)