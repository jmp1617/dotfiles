var MigrationPopupDialog=function(o){Dialog.call(this,o,{submitDialog:!1,confirmOnClose:!1,hideButtons:!0,hideHeader:!0,additionalClasses:"migrationPopupDialog"})};MigrationPopupDialog.prototype=Object.create(Dialog.prototype),MigrationPopupDialog.prototype.constructor=MigrationPopupDialog,function(){MigrationPopupDialog.prototype.initialize=function(o){Dialog.prototype.initialize.apply(this,arguments),function(o){document.getElementById("openVault").onclick=function(){window.open(o.data.url+"vault.html"),o.close()},document.getElementById("closePopup").onclick=function(){o.close()},bg.sendLpImprove("migration::formfill::tour::notification")}(this)}}();